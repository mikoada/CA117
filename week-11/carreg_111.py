from re import findall
import sys

#counties = C|CE|CN|CW|D|DL|G|KE|KK|KY|L|LD|LH|LM|LS|MH|MN|MO|OY|RN|SO|T|W|WH|WX|WW
car = r"\d{2}[12]\s(?:C|CE|CN|CW|D|DL|G|KE|KK|KY|L|LD|LH|LM|LS|MH|MN|MO|OY|RN|SO|T|W|WH|WX|WW)"

def main():
   # Verify regular expression is not overly long
   assert(len(car) < 120)

   s = sys.stdin.read()
    
   carlist = findall(car, s)
   print('Cars: {}'.format(carlist))

if __name__ == '__main__':
    main()