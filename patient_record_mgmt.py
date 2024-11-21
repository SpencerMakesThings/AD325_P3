# Patient Record Management System
# Spencer Kunz

# so I guess this is where we manage all those patient records huh
# wonder how that works

# I spose we're gonna start by making a BST
# Then we'll need some methods for populating it
# 

import graphviz # I think this should be working?
from binary_search_tree import BinarySearchTree, Node

class PatientRecord:
    def __init__(self, patient_id, name, age, diagnosis, blood_pressure,
                           pulse, body_temperature):
        
        self.patient_id = int(patient_id)
        self.name = name
        self.age = age
        self.diagnosis = diagnosis
        self.blood_pressure = blood_pressure
        self.pulse = pulse
        self.body_temperature = body_temperature


    # optional, a method for returning the patient record in a neat format
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
        self.bst = BinarySearchTree()
        self.node_count = 0


    def add_patient_record(self, patient_id, name, age, diagnosis, blood_pressure,
                           pulse, body_temperature):
        # use the passed 
        new_patient_record = PatientRecord(patient_id, name, age, diagnosis,
                                           blood_pressure,pulse, body_temperature)
        # make a node with key=Patient_ID and value=new_patient_record
        new_node = Node(patient_id,new_patient_record)
        # insert the new node
        self.bst.insert(new_node)
        self.node_count += 1


    def search_patient_record(self, patient_id):
        node = self.bst.search(patient_id)
        return node


    def delete_patient_record(self, patient_id):
        self.bst.remove(patient_id)
        self.node_count -= 1


    def display_all_records(self):
        # traverse in order
        # print each patient record
        print("    DISPLAY_ALL_RECORDS")
        inorder_list = self.bst.inorder_traversal(self.bst.root)
        for i in inorder_list:
            node = self.bst.search(i)
            node_val = node.get_value()
            node_val.print_patient_record()
        print(" ")


    def build_tree_from_csv(self, file_path):
        # given the path to CSV
        # puts each line from CSV into tree node
        try:
            with open(file_path, 'r') as file:
                for line in file:

                    line = line.strip()
                    if not line:
                        continue

                    fields = line.split(',')

                    try:
                        patient_id = int(fields[0])
                    except ValueError:
                        continue
                    name = fields[1]
                    age = int(fields[2])
                    diagnosis = fields[3]
                    blood_pressure = fields[4]
                    pulse = int(fields[5])
                    body_temperature = float(fields[6])

                    self.add_patient_record(patient_id,name,age,diagnosis,blood_pressure,pulse, body_temperature)
        except FileNotFoundError: print("File not found")
        except Exception as e: print("Error: ", e)


    def visualize_tree(self):
        # run that graphviz thing
        dot = graphviz.Digraph()
        self._add_nodes(dot, self.bst.root)
        dot.view()
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

    def print_keys_record(self, key):
        node = self.bst.search(key)
        if node is not None:
            pat_rec = node.get_value()
            if pat_rec is not None:
                pat_rec.print_patient_record()
        else:
            print('Record not found')