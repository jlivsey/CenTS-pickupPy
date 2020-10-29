
# deck is data.frame with columns suit, card, value

suits <- c(
  'spade',
  'clubs',
  'heart',
  'dimnd'
)

cards <- c(
  '2', '3', '4', '5', '6', 
  '7', '8', '9', '10', 'J', 'Q', 'K', 'A'
)


deck <- expand.grid(cards, suits)
colnames(deck) <- c('card', 'suit')

values <- c(2:10, c(10, 10, 10, 11))

deck$value <- rep(values, 4)

draw <- function(deck, n = 1){
  idx         <- sample(x = 1:nrow(deck), size = n)
  card_picked <- deck[idx, ]
  upd_deck    <- deck[-idx, ]
  return(list(card_picked = card_picked,
              upd_deck    = upd_deck))
}


starting_pull <- draw(deck, 4)
deck2 <- starting_pull$upd_deck
my_cards <- starting_pull$card_picked[1:2, ]
dealer_cards <- starting_pull$card_picked[3:4, ]

BJcheck <- function(cards){
  if(sum(cards$value) == 21){ 
    return(TRUE)
  } else{
  return(FALSE)
  }
}


