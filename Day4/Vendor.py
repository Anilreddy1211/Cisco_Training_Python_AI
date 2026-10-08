import time


class Vendor:

    def __init__(self, vName, vGST):
        self.vName = vName
        self.vGST = vGST

        print(f"Vendor {self.vName} enrollment is done")

    def billing(self, pName, pQty=0, pCost=0.0):

        # Product details
        self.pName = pName
        self.pQty = pQty
        self.pCost = pCost

        # Calculate total
        self.total = self.pCost * self.pQty

        # Calculate GST 18%
        self.tax = self.total * 0.18

        # Calculate grand total
        self.gs = self.total + self.tax

        # Create log data
        s1 = f"{self.vName}\t{self.vGST}\t{self.pName}\t{self.pQty}"
        s2 = f"\t{self.pCost}\t{self.total}\t{self.gs}"
        s3 = f"\t{time.ctime()}\n\n"

        # Write data to log file
        with open("vendor_prods.log", "a") as wobj:
            wobj.write(s1 + s2 + s3)

        # Display bill
        print("\n----- BILL DETAILS -----")
        print(f"Vendor       : {self.vName}")
        print(f"GST Number   : {self.vGST}")
        print(f"Product      : {self.pName}")
        print(f"Quantity     : {self.pQty}")
        print(f"Cost         : {self.pCost}")
        print(f"Total        : {self.total}")
        print(f"GST (18%)    : {self.tax}")
        print(f"Grand Total  : {self.gs}")
        print(f"Date & Time  : {time.ctime()}")
        print("------------------------")


# Create vendor objects
vobj1 = Vendor("Klabs", "GST1234")
vobj2 = Vendor("Xserver", "GST5593")


# Billing for Klabs
vobj1.billing("pA", 5, 1250)

# Wait for 2 seconds
time.sleep(2)


# Billing for Xserver
vobj2.billing("pB", 2, 435.2)

# Wait for 5 seconds
time.sleep(5)


# Another billing for Klabs
vobj1.billing("pB", 4, 250)