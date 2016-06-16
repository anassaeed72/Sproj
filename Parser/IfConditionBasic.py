import os
import sys
from lxml import etree
import xml.etree.ElementTree
import re
from pymongo import MongoClient
from operator import itemgetter
from collections import OrderedDict
from Print import Print
from Constants import PrintLevel
from xml.dom import minidom

class IfConditionBasic(object):
	"""docstring for IfConditionBasic"""
	def __init__(self, fileName):
		super(IfConditionBasic, self).__init__()
		self.fileName = fileName
	def evaluate(self):				
		xmldoc = minidom.parse(self.fileName)
		collectionValue = "NULL"
		leftValue = ""
		rightValue = ""
		operatorValue = ""
		try:
			left = xmldoc.getElementsByTagName('key')
			leftValue = left[0].attributes['myvalue'].value
		except Exception, e:
			pass
		try:
			right = xmldoc.getElementsByTagName('value')
			rightValue = right[0].attributes['myvalue'].value
		except Exception, e:
			pass
		try:
			collection = xmldoc.getElementsByTagName('collection')
			collectionValue = collection[0].attributes['myvalue'].value
		except Exception, e:
			pass
			
		try:
			operator = xmldoc.getElementsByTagName('operator')
			operatorValue = operator[0].attributes['myvalue'].value
		except Exception, e:
			pass
		

		client = MongoClient()
		db = client.test
		
		if collectionValue=="DOSCollection":
			print ("\nDOS Detection")
			print  ("Operator : " + operatorValue)
			print("Left Hand Side Value : " +leftValue )
			print ("Right Hand Side Value : " +rightValue+"\n")
			cursor = list(db.randCollection.aggregate([
		    {"$group" : {"_id" : "$SenderIP", "count":  { "$sum" : 1}}

		    }
			]))
			if operatorValue=="average":
				countOfDocuments = 0
				countOfPackets = 0
				for document in cursor:
					countOfDocuments = countOfDocuments +1
					countOfPackets+=document["count"]
				averageValue = countOfPackets/countOfDocuments
				if averageValue > int (rightValue):
					Print.Print(PrintLevel.IfConditionAnswerBasic,"true")
					return True
				else:
					Print.Print(PrintLevel.IfConditionAnswerBasic,"false")
					return False
				sys.exit()

			if operatorValue=="sum":
				countOfDocuments = 0
				countOfPackets = 0
				for document in cursor:
					countOfPackets+=document["count"]
				if countOfPackets > int (rightValue):
					Print.Print(PrintLevel.IfConditionAnswerBasic,"true")
					return True
				else:
					Print.Print(PrintLevel.IfConditionAnswerBasic,"false")
					return False
				sys.exit()

			if operatorValue == "greaterThan":
				for document in cursor:
					if document["count"]>=rightValue and document["_id"] == leftValue:
						return True
			
			if operatorValue =="topSenders":
				print "in topSenders"
				client = MongoClient()
				db = client.test
				cursor = list(db.randCollection.aggregate([
				{"$group" : {"_id" : "$SenderIP", "count":  { "$sum" : 1}}
				},
				{"$limit": int(rightValue)}]))
				sumOfPackets = 0;
				IpList= []
				for document in cursor:
					if document["count"] < int(leftValue):

						return False
					IpList.append(document["_id"])

				print ("IPs with more then " + str(leftValue) +" packets")
				for IP in IpList:
					print IP				
				return True
			if operatorValue =="topSendersSum":
				client = MongoClient()
				db = client.test
				cursor = list(db.randCollection.aggregate([
				{"$group" : {"_id" : "$SenderIP", "count":  { "$sum" : 1}}
				},
				{"$limit": int(rightValue)}]))
				sumOfPackets = 0;
				for document in cursor:

					sumOfPackets = sumOfPackets + document["count"]
				if sumOfPackets >= int(leftValue):
					return True
				return False
			for document in cursor:
				# print document
				if document["_id"]== leftValue:
					if document["count"]>=int(rightValue):
						Print.Print(PrintLevel.IfConditionAnswerBasic,"true")
						return True
					else:
						Print.Print(PrintLevel.IfConditionAnswerBasic,"false")
						return False
					sys.exit()
			Print.Print(PrintLevel.IfConditionAnswerBasic,"false")
			return False
			sys.exit()

		if operatorValue =="contains":
			key_ =leftValue# sys.argv[2] # key is col and value is 127.0.0.1
			value =rightValue# sys.argv[3]

			key_val = {}
			key_val[key_] = value

			cursor = db[collectionValue].find(key_val)
			Print.Print(PrintLevel.NewLine,"")
			Print.Print(PrintLevel.IfConditionFormatting, "If Condition Evaluation")
			Print.Print(PrintLevel.IfConditionFormatting, "Key:  " + key_)
			Print.Print(PrintLevel.IfConditionFormatting, "Value:  " + value)
			Print.Print(PrintLevel.IfConditionFormatting, "Operation:  Contains")


			if cursor.count() >0:
				Print.Print(PrintLevel.IfConditionAnswerBasic,"true")
				return True
			else:
				Print.Print(PrintLevel.IfConditionAnswerBasic,"false")
				return False 
			sys.exit()
		if operatorValue == "Inversion":
			print " in Inversion"
			innerCollection = xmldoc.getElementsByTagName('innerCollection')
			outerCollection = xmldoc.getElementsByTagName('outerCollection')
			innerCollectionField = xmldoc.getElementsByTagName('innerCollectionField')
			outerCollectionField = xmldoc.getElementsByTagName('outerCollectionField')

			innerCollectionValue = innerCollection[0].attributes['myvalue'].value
			outerCollectionValue = outerCollection[0].attributes['myvalue'].value
			innerCollectionFieldValue = innerCollectionField[0].attributes['myvalue'].value
			outerCollectionFieldValue = outerCollectionField[0].attributes['myvalue'].value
			Print.Print(PrintLevel.IfConditionFormatting,"If Condition Evaluation")
			Print.Print(PrintLevel.IfConditionFormatting,"Operation : Inversion")
			Print.Print(PrintLevel.IfConditionFormatting,"Inner Collection : " +innerCollectionValue)
			Print.Print(PrintLevel.IfConditionFormatting,"Inner Collection Field : " +innerCollectionFieldValue)
			Print.Print(PrintLevel.IfConditionFormatting,"Output Collection : " + outerCollectionValue)
			Print.Print(PrintLevel.IfConditionFormatting,"Output Collection Field : " +outerCollectionFieldValue )
			cursor = db[outerCollectionValue].find()
			for document in cursor:
				if self.findObjectInCollectionAbsent(innerCollectionValue,innerCollectionFieldValue,document[outerCollectionFieldValue]):
					print ("Process Found is : " + document[outerCollectionFieldValue])
					return True
		return False

	def findObjectInCollectionAbsent(self,collection,toFindField,toFindValue):
		client = MongoClient()
		db = client.test
		cursor = db[collection].find({toFindField:toFindValue})
		for document in cursor:
			return False
		return True