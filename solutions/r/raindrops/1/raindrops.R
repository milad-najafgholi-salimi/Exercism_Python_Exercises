raindrops <- function(number) {
  printed <- FALSE
  output <- ""
  
  if (number %% 3 == 0){
    output <- paste0(output, "Pling")
    printed <- TRUE
  }
  if (number %% 5 == 0){
    output <- paste0(output, "Plang")
    printed <- TRUE
  }
  if (number %% 7 == 0){
    output <- paste0(output, "Plong")
    printed <- TRUE
  }
  if (!printed) {
    output <- as.character(number)
  }
  return (output)
}
