#!/usr/bin/env python

from textwrap import dedent
import math


# In memory representation of the donor database
donor_db = {
   "William Gates, III": [653772.32,  12.17],
   "Jeff Bezos": [877.33],
   "Paul Allen": [663.23, 43.87, 1.32]
}


def main_menu_selection():
   """
   Print out the main application menu and then read the user input.
   """
   input = raw_input(dedent('''
      Choose an action:

      1 - Send a Thank You
      2 - Create a Report
      3 - Quit

      > '''))
   return input.strip()


def send_thank_you():
   """
   Execute the logic to record a donation and generate a thank you message.
   """
   # Read a valid donor to send a thank you from, handling special commands to
   # let the user navigate as defined.
   name = None
   while True:
      name = raw_input("Enter a donor's name (or list to see all donors or 'menu' to exit)> ").strip()
      if name == "list":
         print "Donor list:\n"
         print [name for name in donor_db.iterkeys()]
      elif name == "menu":
         return
      else:
         break

   # Now prompt the user for a donation amount to apply. Since this is also an exit
   # point to the main menu, we want to make sure this is done before mutating the db
   # dictionary object.
   amount = 0.0
   while True:
      amount_str = raw_input("Enter a donation amount (or 'menu' to exit)> ").strip()
      if amount_str == "menu":
         return
      # Make sure amount is a valid amount before leaving the input loop
      amount = float(amount_str)
      if math.isnan(amount) or math.isinf(amount) or round(amount, 2) == 0.00:
         print "error: donation amount is invalid\n"
      else:
         break

   # If this is a new user, ensure that the database has the necessary data structure.
   if name not in donor_db:
      donor_db[name] =  []

   # Record the donation and generate a thank you message
   donor_db[name].append(amount)
   print dedent('''
      Dear %s

      Thank you for your very kind donation of %s.
      ''' % (name, amount))


def print_donor_report():
   """
   Generates the report of the donors and amounts donated.
   """
   # First, reduce the raw data points into a summary list view
   report_rows = []
   for (name, gifts) in donor_db.items():
      total_gifts = round(sum(gifts), 2)
      num_gifts = len(gifts)
      avg_gift = round(total_gifts / num_gifts, 2)
      report_rows.append( (name, total_gifts, num_gifts, avg_gift) )

   # Now output the summary list view in a sorted order
   cmp_total_gifts = lambda x,y: cmp(x[1], y[1])
   for (name, total, num_gifts, avg_gift) in [("Name", "Total", "Num", "Avg.")] + sorted(report_rows, cmp_total_gifts):
      print repr(name).ljust(30), repr(total).rjust(12), repr(num_gifts).rjust(4),
      print repr(avg_gift).rjust(12)


if __name__ == "__main__":
   running = True
   while running:
      selection = main_menu_selection()
      if selection is "1":
         send_thank_you()
      elif selection is "2":
         print_donor_report()
      elif selection is "3":
         running = False
      else:
         print "error: menu selection is invalid!"
