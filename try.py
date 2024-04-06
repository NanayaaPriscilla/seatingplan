
class GalaDinnerManager:
    def __init__(self):
        self.groups = []
        self.tables = {'6': [], '8': []}
        self.total_attendees = 0
        self.vacanciesfortable8=[]
        self.vacanciesfortable6=[]
        

    def enter_groups(self):
        num_groups = int(input("Enter the number of groups attending the event: "))
        for i in range(num_groups):
            group_size = int(input(f"Enter the size of group {i + 1}: "))
            self.groups.append(group_size)
            self.total_attendees += group_size
            total =self.total_attendees
            print(total)

    def create_seating_plan(self):

        for group in sorted(self.groups,reverse=True):
            if group == 6:
                self.tables['6'].append(group)
                print(f"Capacity 6 Table{len(self.tables['6'])}:Group{group}")
            elif group == 5:
               self.tables['8'].append(group)
               print(f"Capacity 8 Table{len(self.tables['8'])}:Group{group},Vacant seats{len(self.tables['8'])} : 3 seats")
               num8=int(len(self.tables['8']))
            elif group == 4:        
                 self.tables['6'].append(group)
                 print(f"Capacity 6 Table{len(self.tables['6'])}:Group{group},Vacant seats{len(self.tables['6'])} : 2 seats ")
                 num6=int(len(self.tables['6']))

            elif group == 2:
                        if 4 in sorted(self.groups,reverse=True):
                         self.vacanciesfortable6.append(group)
                         print(f"Capacity 6 Vacant seats {len(self.vacanciesfortable6)}: Group {group}")
                         count4 =self.groups.count(4)
                         count2 = self.groups.count(2)
                         unpaired_group2 =count2 - count4
                         if count4 and unpaired_group2 > 0:
                           self.vacanciesfortable6 .append(group)
                           print(f"Capacity 6 Vacant seats {len(self.vacanciesfortable6)}: Group {group}")
                           self.tables['6'].append(unpaired_group2)
                           print(f"{unpaired_group2} group {group}s assigned to capacity 6 Table{len(self.tables['6'])}")
                           break
                        else :
                        
                         count = self.groups.count(2)
                        
                         if count <= 3:
                             print(f"{count} group {group}s assigned to capacity 6 Table {len(self.tables['6'])}")
                            
                         else :
                          self.tables['8'].append(group)   
                          print(self.tables['8'])
                          print(f"{count} of group {group}s assigned to capacity 8 Table {len(self.tables['8'])}")
                          
                         

            elif group == 3:
                if 5 in sorted(self.groups,reverse = True):
                     self.vacanciesfortable8.append(group)
                     print(f"Capacity 8 Vacant seats {len(self.vacanciesfortable8)} : Group {group}")
                     count5 =self.groups.count(5)
                     count3 = self.groups.count(3)
                     unpaired_group3 =count3- count5
                     if count5 and unpaired_group2 > 0:
                           self.vacanciesfortable6 .append(group)
                           print(f"Capacity 8 Vacant seats {len(self.vacanciesfortable6)}: Group {group}")
                           self.tables['6'].append(unpaired_group3)
                           print(f"{unpaired_group3} group {group}s assigned to capacity 6 Table{len(self.tables['6'])}")
                           
                else :
                    for i in self.groups:
                
                     count3 = self.groups.count(3)
                     if count3 <= 2:
                       self.tables['6'].append(2)
                       print(f"{count3} group{group}s assigned to capacity 6 Table {len(self.tables['6'])}")
                     elif count3 == 3:
                        self.tables['6'].append(2)
                        print(f"2 group{group}s assigned to capacity 6 Table {len(self.tables['6'])}")
                        self.tables['6'].append(1)
                        print(f"1 group{group} assigned to capacity 6 Table{len(self.tables['6'])},Vacant seats{len(self.vacanciesfortable6)}")
                    
                     elif count3 == 4:
                         self.tables['6'].append(2)
                         print(f"2 group{group}s assigned to capacity 6 Table {len(self.tables['6'])}") 
                         self.tables['6'].append(2)
                         print(f"2 group{group}s assigned to capacity 6 Table {len(self.tables['6'])}")
                         
                     

            else:
                print("INVALID")
            
        
                     
            
                         

              

    def display_menu(self):
        print("\nMenu:")
        print("1. Enter the number of groups attending the event")
        print("2. Create seating plan")
        print("3. Exit")

    def main(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                self.enter_groups()
            elif choice == '2':
                self.create_seating_plan()
            elif choice == '3':
                print("Exiting program...")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    manager = GalaDinnerManager()
    manager.main()
