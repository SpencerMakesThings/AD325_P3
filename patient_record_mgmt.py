# Patient Record Management System
# Spencer Kunz

import graphviz # <--- this was the hardest part of the entire project
from binary_search_tree import BinarySearchTree, Node

class PatientRecord:
    def __init__(self, patient_id, name, age, diagnosis, blood_pressure,
                           pulse, body_temperature):
        
        # Variables to make a patient record
        # patient_id is specced as an int bc it was being compared as a string before
        # and that caused the inorder_traverse to come out wonky
        self.patient_id = int(patient_id)
        self.name = name
        self.age = age
        self.diagnosis = diagnosis
        self.blood_pressure = blood_pressure
        self.pulse = pulse
        self.body_temperature = body_temperature


    # a method for returning the patient record in a neat-ish format
    def print_patient_record(self):
        print(self.patient_id, self.name, self.age, self.diagnosis,
              self.blood_pressure, self.pulse, self.body_temperature)
        """
        print("Patient ID:       ", self.patient_id)
        print("Name:             ", self.name)
        print("Age:              ", self.age)
        print("Diagnosis:        ", self.diagnosis)
        print("Blood Pressure:   ", self.blood_pressure)
        print("Pulse:            ", self.pulse)
        print("Body Temperature: ", self.body_temperature)
        print(" ")
        """


class PatientRecordManagementSystem:

    def __init__(self):
        self.bst = BinarySearchTree()   # a tree to hold the records
        self.node_count = 0             # i thought about adding get_count methods
                                        # but they turned out to be unnecessary
                                        # Could still add those features later
    def add_patient_record(self, patient_id, name, age, diagnosis, blood_pressure,
                           pulse, body_temperature):
        # use the passed patient info to make a PatientRecord item
        new_patient_record = PatientRecord(patient_id, name, age, diagnosis,
                                           blood_pressure,pulse, body_temperature)
        # make a node with key=Patient_ID and value=new_patient_record
        new_node = Node(patient_id,new_patient_record)
        # insert the new node
        self.bst.insert(new_node)
        self.node_count += 1    # increment count


    def search_patient_record(self, patient_id):    
        node = self.bst.search(patient_id)          # just uses the BST method
        return node


    def delete_patient_record(self, patient_id):
        self.bst.remove(patient_id)                 # uses the BST remove
        self.node_count -= 1                        # decrement count


    def display_all_records(self):              
        # traverse in order
        # print each patient record
        print("    DISPLAY_ALL_RECORDS")  # first get list from inorder_traverse method
        inorder_list = self.bst.inorder_traversal(self.bst.root)# put it in a variable
        for i in inorder_list:                                  # for each list entry
            node = self.bst.search(i)                           # get entry from tree
            node_val = node.get_value()                         # get value from entry
            node_val.print_patient_record()                     # value is a PatRecord
        print(" ")                                              # call PR print method


    def build_tree_from_csv(self, file_path):
        # given the path to CSV
        # puts each line from CSV into tree node
        try:                                    
            with open(file_path, 'r') as file:      # open the file at specd path
                for line in file:                   # for each line in the file
                    line = line.strip()             # strip whitespace
                    if not line:                    # if line is empty
                        continue                    # skip

                    datas = line.split(',')         # split at the commas
                    try:# this is just here because of the .csv's first line
                        patient_id = int(datas[0])  # first piece of data is PatID
                    except ValueError:              # if patient id isn't an int
                        continue                    # bad line; skip it
                    name = datas[1]                 # fill the rest of the datas
                    age = int(datas[2])
                    diagnosis = datas[3]
                    blood_pressure = datas[4]
                    pulse = int(datas[5])
                    body_temperature = float(datas[6])
                    # then use the datas to add a new PatRec
                    self.add_patient_record(patient_id,name,age,diagnosis,blood_pressure,pulse, body_temperature)
        
        except FileNotFoundError: print("File not found")   # error handling
        except Exception as e: print("Error: ", e)


    def visualize_tree(self):
        # run that graphviz thing
        dot = graphviz.Digraph()
        self._add_nodes(dot, self.bst.root)
        dot.view()  # added this to view the tree
        return dot

    def _add_nodes(self, dot, node):
        if node:
            dot.node(str(node.key), f"{node.key}: {node.value.name}")
            if node.left:
                dot.edge(str(node.key), str(node.left.key))
                self._add_nodes(dot, node.left)
            if node.right:
                dot.edge(str(node.key), str(node.right.key))
                self._add_nodes(dot, node.right)

    def print_keys_record(self, key):   # extra method for printing from main
                                        # cause that was causing boucoup TypeErrors
        node = self.bst.search(key)     # get the specified node
        if node is not None:            # if it's found
            pat_rec = node.get_value()  # get_value it
            if pat_rec is not None:     # if get_value is successful (PatRec found)
                pat_rec.print_patient_record()  # call PatientRecord's print method
        else:
            print('Record not found')