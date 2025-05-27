from model import ShopList
from view import ShopView
from controller import ShopController

if __name__ == "__main__":

    shop_list = ShopList()
    shop_view = ShopView()
    shop_controller = ShopController(shop_list, shop_view)

    shop_controller.run()