score <- function(x, y) {
  y2 <- (x^2 + y^2)

  if (y2 <= 1){
    return (10)
  }
  else if (y2 > 1 && y2 <= 25){
    return (5)
  }
  else if (y2 > 25 && y2 <= 100){
    return (1)
  }
  else{
    return (0)
  }
}
