#Python program for money requirment for painting  a cuboidal box
#Dimensions of the box in meters 
length = 5
breadth = 8
height = 6

#Surface areas of sides 
Front_back_sides = 2*(length * height)
Top_bottom_sides = 2*(length * breadth)
Left_right_sides = 2*(breadth * height)
Total_surface_area = Front_back_sides + Top_bottom_sides + Left_right_sides

Costofpaint_per_litre = 100 #Cost in Rupees 
Area_covered_per_litre = 10 #Area in meters

Amount_of_paint_required = Total_surface_area / Area_covered_per_litre

Amount_of_money_required = Amount_of_paint_required * Costofpaint_per_litre 
print("The Total surface area of box to be painted : {} ".format(Total_surface_area))
print("Amount of paint required for painting the box: {}  ".format(Amount_of_paint_required))
print("Total Money required for painting the box : {} ".format(Amount_of_money_required))
