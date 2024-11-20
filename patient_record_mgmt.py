# Patient Record Management System
# Spencer Kunz

# so I guess this is where we manage all those patient records huh
# wonder how that works

# I spose we're gonna start by making a BST
# Then we'll need some methods for populating it
# 

import graphviz
from binary_search_tree import BinarySearchTree, Node
from patient_record_mgmt import PatientRecord



class PatientRecord:
    def __init__(self, patient_id, name, age, diagnosis, blood_pressure,
                           pulse, body_temperature):
        
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.diagnosis = diagnosis
        self.blood_pressure = blood_pressure
        self.pulse = pulse
        self.body_temperature = body_temperature

    # optional, a method for returning the patient record in a neat format
    def print_patient_record(self):

        print("Patient ID:       ", self.patient_id)
        print("Name:             ", self.name)
        print("Age:              ", self.age)
        print("Diagnosis:        ", self.diagnosis)
        print("Blood Pressure:   ", self.blood_pressure)
        print("Pulse:            ", self.pulse)
        print("Body Temperature: ", self.body_temperature)





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
        return self.bst.search(patient_id)


    def delete_patient_record(self, patient_id):
        self.bst.remove(patient_id)
        self.node_count -= 1


    def display_all_records(self):

        pass


    def build_tree_from_csv(self, file_path):
        # given the path to CSV
        # puts each line from CSV into tree node
        pass


    def vizualize_tree(self):
        # run that graphviz thing
        dot = graphviz.Digraph()
        self._add_nodes(dot, self.bst.root)
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

