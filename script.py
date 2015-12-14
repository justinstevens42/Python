from collections import defaultdict

class Dictlist(dict):
    def __setitem__(self, key, value):
        try:
            self[key]
        except KeyError:
            super(Dictlist, self).__setitem__(key, [])
        self[key].append(value)
def ask_yes_no(question):
    response=None
    while response not in ("y", "n"):
    	response=raw_input(question).lower()
   	return response
def main():
	g=open(****CLASSNAME <-MODIFY THIS****, 'r')
	d={}
	g.seek(0)
	d=g.readlines()
	Points_Received=0
	Points_Total=0
	total=0
	Points_Received=Dictlist()
	Points_Total=Dictlist()
	for i in range(len(d)):
	
		#all of this is weird formatting stuff and can be ignored
		sep='/'
		sep2='\t'
		sep3='\t\t\t\t\t\t'
		first=d[i].split(sep2, 1)[1] #get rid of the date
		category=first.split(sep2, 1)[0] #find the category of the assignment
		temp=first.split(sep3, 1)[1] #get rid of all the indents because nobody cares
		PR=temp.split(sep, 1)[0]  #find the points you received on the assignment and make it a float
		PR=float(PR)
		Points_Received[category]=PR
		new=temp.split(sep, 1)[1]  #find everything after the "/" in the grade
		PT=new.split(sep2,1)[0]  #find the grade you received on the assignment
		PT=float(PT)
		Points_Total[category]=PT
	Category_PR={}  #create a new variable for the points received for each category
	for key in Points_Received:
		Category_PR[key]=sum(Points_Received[key])
	Category_PT={}
	for key in Points_Total:
		Category_PT[key]=sum(Points_Total[key])
	response=ask_yes_no("Are there special weightings for your class? (y/n)")
	if response=='y':
		Weighting={}
		for key in Points_Total:
			print "What fraction of your grade is",key,"? (enter a decimal)"
			r=float(raw_input(""))
			
			Weighting[key]=r 
		Final_Grade=0
		for key in Points_Total:
			print "The grade you currently have for",key,"(",100*Weighting[key],"%) is",round(Category_PR[key],3), "/", Category_PT[key], "or",  Category_PR[key]/Category_PT[key]
			Final_Grade=Final_Grade+100*Weighting[key]*Category_PR[key]/Category_PT[key]
		print "\n"
		print "Your total grade in the class is currently ", Final_Grade 
	if response=='n':
		Total_PR=0
		Total_PT=0
		for key in Points_Received:
			Total_PR=Total_PR+Category_PR[key]
		for key in Points_Total:
			Total_PT=Total_PT+Category_PT[key]
		print "Your total grade in the class is currently ", Total_PR, "/", Total_PT, "or ", 100*Total_PR/Total_PT, "%"

main()
