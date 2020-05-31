library(shiny)
library(leaflet)
library(ggmap)
library(dplyr)
library(reticulate)

###################################################
# Support functions
###################################################

# Convert kelvin to celsius
to_celsius <- function(kelvin) {
  return(as.integer(as.numeric(kelvin) - 273.15))
}

# Serch for wor in df with closest distance to lat,lng
find_clicked_row <- function(df, lat, lng) {
  if (nrow(df) == 0) {
    return(0)
  }
  min_row <- 0
  min_delta <- 0
  for (i in 1:nrow(df)) {
    delta <- abs(lat - df$lat[i]) + abs(lng - df$lng[i])
    if (delta < 2 & (delta < min_delta | min_row == 0)) {
      min_row <- i
      min_delta <- delta
    }
  }
  
  return(min_row)
}

###################################################
# Python interface function
###################################################

# Retrieve dive sites around lat,long within distance dist
dive_api <- function(lat, lon, dist) {
  import("urllib.request")
  source_python("apis/dive_api.py")
  py_string <-
    sprintf("sites=dive_sites_string_R(%f, %f,%f)", lat, lon, dist)
  
  py_run_string(py_string)
  py$sites
}

# Retrieve whale sightings around lat,long within distance dist with max_whales as limit
whale_api <- function(lat, lon, dist, max_whales) {
  import("urllib.request")
  source_python("apis/whale_api.py")
  py_string <-
    sprintf("whales=whale_sightingss_string_R(%f, %f, %f, %d)",
            lat,
            lon,
            dist,
            max_whales)
  
  py_run_string(py_string)
  py$whales
}

# Retrieve weather data at lat,lon
weather_api <- function(lat, lon) {
  import("urllib.request")
  source_python("apis/weather_openweathermap_api.py")
  py_string <-
    sprintf("forecasts=weather_forecast_string_R(%f, %f)", lat, lon)
  
  py_run_string(py_string)
  py$forecasts
}

# Dive site app server logic
server <- function(input, output) {
  # observer function for location input changes
  observe({
    input$location
    # determine latitude and longitude via google maps geocoding service
    lat_lon <- list(lon = NA,
                    lat = NA,
                    address = "")
    if (input$location != "") {
      register_google(key = "AIzaSyAmz9ywp4S7zEsonrgN7VhpUQt7tbrmGaY")
      lat_lon <-
        geocode(input$location, output = "latlona", source = "google")
    }
    lat_lon[is.na(lat_lon)] <- 0
    
    # display coordinates
    output$coordinates <- renderText({
      paste(lat_lon$lon, lat_lon$lat)
    })
    
    # call dive site api and convert result to data frame
    sites <- dive_api(lat_lon$lat, lat_lon$lon, input$dist / 5)
    dive_sites <- read.csv(text = sites)
    dive_sites$lat <-  as.numeric(dive_sites$lat)
    dive_sites$lng <-  as.numeric(dive_sites$lng)
    
    # call whale sightings api and convert result to data frame
    whales <- whale_api(lat_lon$lat, lat_lon$lon, 20, input$dist)
    whales <- read.csv(text = whales)
    whales$lat <-  as.numeric(whales$lat)
    whales$lng <-  as.numeric(whales$lng)
    
    # colors for leaflet map
    pal <-
      colorFactor(
        pal = c("#0000FF", "#dc143c"),
        domain = c("Dive Site", "Whale Sighting")
      )
    
    # draw leaflet map
    output$divemap <- renderLeaflet({
      input$location
      input$dist
      leaflet() %>%
        # around entered location
        fitBounds(
          lat_lon$lon - input$dist / 232,
          lat_lon$lat - input$dist / 232,
          lat_lon$lon + input$dist / 232,
          lat_lon$lat + input$dist / 232
        ) %>%
        addTiles() %>%
        # draw dive site markers
        addCircleMarkers(
          data = dive_sites,
          lat =  ~ lat,
          lng =  ~ lng,
          radius = 6,
          color = ~ pal("Dive Site"),
          stroke = FALSE,
          fillOpacity = 0.8
        ) %>%
        # draw whale markers
        addCircleMarkers(
          data = whales,
          lat =  ~ lat,
          lng =  ~ lng,
          radius = 6,
          color = ~ pal("Whale Sighting"),
          stroke = FALSE,
          fillOpacity = 0.8
        ) %>%
        # add legend
        addLegend(
          pal = pal,
          values = c("Dive Site", "Whale Sighting"),
          opacity = 1,
          title = "Select location:"
        )
    })
    
    # Mouse click event
    observeEvent(input$divemap_marker_click, {
      p <- input$divemap_marker_click
      
      # find close dive site
      dive_row_no <- find_clicked_row(dive_sites, p$lat, p$lng)
      
      # display site attributes in side bar
      
      # print dive site name
      if (dive_row_no > 0) {
        output$divename <- renderText({
          toString(dive_sites[dive_row_no, ]$name)
        })
      }
      
      # print dive site current
      if (dive_row_no > 0) {
        output$divecurrents <- renderText({
          toString(dive_sites[dive_row_no, ]$currents)
        })
      }
      
      # print dive site description
      if (dive_row_no > 0) {
        output$divedescription <- renderText({
          toString(dive_sites[dive_row_no, ]$description)
        })
      }
      
      # print dive site hazards
      if (dive_row_no > 0) {
        output$divehazards <- renderText({
          toString(dive_sites[dive_row_no, ]$hazards)
        })
      }
      
      # print dive site marine life
      if (dive_row_no > 0) {
        output$divemarinelife <- renderText({
          toString(dive_sites[dive_row_no, ]$marinelife)
        })
      }
      
      # print dive site max depth
      if (dive_row_no > 0) {
        output$divemaxdepth <- renderText({
          toString(dive_sites[dive_row_no, ]$maxdepth)
        })
      }
      
      # find close whale sightings
      whale_row_no <- find_clicked_row(whales, p$lat, p$lng)
      
      # display sighting attributes in side bar
      
      # print whale species
      if (whale_row_no > 0) {
        output$whalespecies <- renderText({
          toString(whales[whale_row_no, ]$species)
        })
      } else {
        output$whalespecies <- renderText({
          ""
        })
      }
      
      # print whale sighting date
      if (whale_row_no > 0) {
        output$whalesightedat <- renderText({
          toString(whales[whale_row_no, ]$sighted_at)
        })
      } else {
        output$whalesightedat <- renderText({
          ""
        })
      }
      
      # get weather date for clicked location
      forecast <- weather_api(p$lng, p$lat)
      forecast <- read.csv(text = forecast)
      
      # display weather attributes in side bar
      
      # display weather icon
      if (forecast$icon != "") {
        output$weathericon <- renderUI({
          HTML(
            paste(
              '<div style="background-color: lightblue">
              <img src="http://openweathermap.org/img/wn/',
              forecast$icon,
              '@4x.png"',
              'alt="Text Book"/></div>',
              sep = ""
            )
          )
        })
      }
      
      # display main weather
      output$weather <- renderText({
        toString(forecast$main)
      })
      
      # display temperatures
      output$temperature <- renderText({
        paste(
          to_celsius(forecast$temp_min),
          to_celsius(forecast$temp_max),
          to_celsius(forecast$feels_like),
          sep = " / "
        )
      })
      
      #display wind
      output$windDegSpeed <- renderText({
        paste(forecast$wind_speed, forecast$wind_deg, sep = " / ")
      })
      
      #display overcast percentage
      output$cloudsAll <- renderText({
        toString(forecast$clouds_all)
      })
    })
  })
}
