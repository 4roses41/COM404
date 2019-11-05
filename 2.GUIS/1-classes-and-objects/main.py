from bot import Bot
from SuperBot import SuperBot
#from FlyingBot import FlyingBot


bot1 = Bot("bot" , 35, 10, 10,  ) 
superbot1 = SuperBot("flight")
#flyingbot1 = FlyingBot(5)

bot1.display_name()
bot1.display_age()
bot1.display_energy()
bot1.display_shield()
superbot1.display_super_power()

#flyingbot1.hover_distance()