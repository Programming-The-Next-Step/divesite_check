library(shiny)
library(leaflet)

# Define UI for dive site app 
ui <- fluidPage(
  titlePanel("Where do you want to dive today?"),
  
  # Sidebar layout
  sidebarLayout(
    sidebarPanel(
      # Location input
      textInput("location", "Location", "Vancouver"),
      
      # Display coordinates
      h5(strong("Coordinates:")),
      h5(textOutput("coordinates")),
      
      # Scaling slider
      sliderInput(
        inputId = "dist",
        label = "Distance (km):",
        min = 1,
        max = 1000,
        value = 500
      ),
      
      # Dive site info
      h2(strong("Dive Site")),
      h3(textOutput("divename")),

      # 
      # Whale info
      h2(strong("Whale Sighting")),
      h5(strong("Species:")),
      h5(textOutput("whalespecies")),
      h5(strong("Sighted at:")),
      h5(textOutput("whalesightedat")),
      # 
      # Wheather info
      h2(strong("Wheater")),
      # Weather icon
      htmlOutput("weathericon"),
      h5(strong("Weather:")),
      h5(textOutput("weather")),
      h5(strong("Temperature (now/min/max/feels):")),
      h5(textOutput("temperature")),
      h5(strong("Wind (speed/direction):")),
      h5(textOutput("windDegSpeed")),
      h5(strong("Clouds (%):")),
      h5(textOutput("cloudsAll")),
      
      # Dive site details
      h2(strong("Site Details")),
      h5(strong("Currents:")),
      h5(textOutput("divecurrents")),
      h5(strong("Description:")),
      h5(textOutput("divedescription")),
      h5(strong("Hazards:")),
      h5(textOutput("divehazards")),
      h5(strong("Marinelife:")),
      h5(textOutput("divemarinelife")),
      h5(strong("Maxdepth:")),
      h5(textOutput("divemaxdepth"))
    ),
    
    # Main panel
    mainPanel(leafletOutput("divemap", height =
                              1000))
  )
)


