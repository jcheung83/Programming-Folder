import store
import product

store = store.Store("Walmart")
bananas = product.Product("bananas", 0.69, "fruit", 0)
apples = product.Product("apples", 0.88, "fruit", 1)
cherries = product.Product("cherries", 3.11, "fruit", 2)
toilet_paper = product.Product("toilet paper", 1.50, "household items", 3)
playstation_5 = product.Product("Playstation 5", 500, "video games", 4)
store.add_product(bananas).add_product(apples).add_product(toilet_paper).add_product(toilet_paper).add_product(playstation_5).add_product(cherries)
store.set_clearance("fruit", 0.50).display_info()
store.sell_product(2).sell_product(3).display_info()
store.inflation(.05).display_info()
