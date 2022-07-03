

def main():
	# write your code here

	num = input('Enter a number from 1 to 12: ')
	noun = input('Enter a noun (plural): ')
	name= input('Enter a name: ')
	sentence = input('Enter any sentence: ')
	verb = input('Enter a verb: ')
	print("The Story goes...\n")
	print("It was "+ num+" o'clock when I heard a knock at the door.")
	print("I opened the door and there was a box full of "+noun+" with a note saying "+"\"From Mr. "+name.capitalize()+".\"")
	print("Just as I closed the door I heard a \""+sentence.upper()+".\"")
	print("I froze in place and all I could do was "+verb+".")
  

if __name__ == '__main__':
	main()