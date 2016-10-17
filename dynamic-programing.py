	
def recMC(coinValueList,change):
   minCoins = change
   if change in coinValueList:
     return 1
   else:
      for i in [c for c in coinValueList if c <= change]:
         numCoins = 1 + recMC(coinValueList,change-i)
         print "numcoins",numCoins
         print "mincoins",minCoins
         if numCoins < minCoins:
            minCoins = numCoins
            print "mincoins in if",minCoins
            print "numcoins in if",numCoins
   return minCoins

print(recMC([1,5,10,25],7))
