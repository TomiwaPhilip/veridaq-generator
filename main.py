from flask import Flask, request
from veridaqRequests.alumniReference import generateAlumniReference
from veridaqRequests.docVerification import generateDocVerification
from veridaqRequests.individualReference import generateIndividualReference
from veridaqRequests.memberReference import generateMemberReference
from veridaqRequests.studentStatus import generateStudentStatus
from veridaqRequests.workReference import generateWorkReference
from veridaqRequests.utils import split_text_to_lines, drawLines

app = Flask(__name__)

@app.route('/doc-verification', methods=["POST"])
def getDoc1():
    if request.method == "POST" and request.is_json:
        try:
            data = request.json  # Access the JSON data from the request
            # Extract required fields from the JSON data
            nameOfOrganization = data["nameOfOrganization"]
            nameOfIndividual = data["nameOfIndividual"]
            documentType = data["documentType"]
            documentName = data["documentName"]
            documentID = data["documentID"]
            nameOfAdmin = data["nameOfAdmin"]
            adminDesignation = data["adminDesignation"]
            currentDateTime = data["currentDateTime"]
            badgeID = data["badgeID"]

            moreInfo = data.get("moreInfo", "NIL")
            
            # Generate the PDF using the received data
            return generateDocVerification(nameOfOrganization, nameOfIndividual, documentType, documentName, documentID, 
                                            moreInfo, nameOfAdmin, adminDesignation, currentDateTime, badgeID)
        except KeyError as e:
            return f"Missing required field: {e}", 400
    else:
        return "Only GET requests with JSON data are allowed", 400


@app.route('/work-reference', methods=["POST"])
def getDoc2():
    if request.method == "POST" and request.is_json:
        try:
            data = request.json  # Access the JSON data from the request
            # Extract required fields from the JSON data
            nameOfEmployee = data["nameOfEmployee"]
            employeeID = data["employeeID"]
            employeeStatus = data["employeeStatus"]
            subType = data["subType"]
            designation = data["designation"]
            department = data["department"]
            period = data["period"]
            jobFunctions = data["jobFunctions"]
            nameOfAdmin = data["nameOfAdmin"]
            badgeID = data["badgeID"]

            nameOfInstitution = data.get("nameOfInstitution", "NIL")
            adminDesignation = data.get("adminDesignation", "NIL")
            currentDateTime = data.get("currentDateTime", "NIL")
            notableAchievement = data.get("notableAchievement", "NIL")
            personalitySummary = data.get("personalitySummary", "NIL")
            
            # Generate the PDF using the received data
            return generateWorkReference(nameOfEmployee, employeeID, employeeStatus, nameOfInstitution, subType, 
                                          designation, department, period, jobFunctions, notableAchievement, 
                                          personalitySummary, nameOfAdmin, adminDesignation, currentDateTime, badgeID)
        except KeyError as e:
            return f"Missing required field: {e}", 400
    else:
        return "Only GET requests with JSON data are allowed", 400


@app.route('/student-status', methods=["POST"])
def getDoc3():
    if request.method == "POST" and request.is_json:
        try:
            data = request.json  # Access the JSON data from the request
            # Extract required fields from the JSON data
            nameOfStudent = data["nameOfStudent"]
            studentID = data["studentID"]
            nameOfInstitution = data["nameOfInstitution"]
            passportUrl = data["passportUrl"]
            categoryOfStudy = data["categoryOfStudy"]
            currentLevel = data["currentLevel"]
            courseOfStudy = data["courseOfStudy"]
            faculty = data["faculty"]
            yearOfEntryAndExit = data["yearOfEntryAndExit"]
            nameOfAdmin = data["nameOfAdmin"]
            adminDesignation = data["adminDesignation"]
            currentDateTime = data["currentDateTime"]
            badgeID = data["badgeID"]
            
            # Generate the PDF using the received data
            return generateStudentStatus(nameOfStudent, studentID, nameOfInstitution, passportUrl, categoryOfStudy, 
                                          currentLevel, courseOfStudy, faculty, yearOfEntryAndExit, nameOfAdmin, 
                                          adminDesignation, currentDateTime, badgeID)
        except KeyError as e:
            return f"Missing required field: {e}", 400
    else:
        return "Only GET requests with JSON data are allowed", 400



@app.route('/individual-reference', methods=["POST"])
def getDoc4():
    if request.method == "POST" and request.is_json:
        try:
            data = request.json  # Access the JSON data from the request
            # Extract required fields from the JSON data
            individualName = data["individualName"]
            issuerName = data["issuerName"]
            relationship = data["relationship"]
            yearsOfRelationship = data["yearsOfRelationship"]
            personalityReview = data["personalityReview"]
            recommendationStatement = data["recommendationStatement"]
            issuerDesignation = data["issuerDesignation"]
            issuerContact = data["issuerContact"]
            currentDateTime = data["currentDateTime"]
            badgeID = data["badgeID"]

            issuerName = data.get("issuerName", "To Whom It May Concern")
            
            # Generate the PDF using the received data
            return generateIndividualReference(individualName, issuerName, relationship, yearsOfRelationship, personalityReview, 
                                            recommendationStatement, issuerDesignation, issuerContact, currentDateTime, badgeID)
        except KeyError as e:
            return f"Missing required field: {e}", 400
    else:
        return "Only GET requests with JSON data are allowed", 400


@app.route('/member-reference', methods=["POST"])
def getDoc5():
    if request.method == "POST" and request.is_json:
        try:
            data = request.json  # Access the JSON data from the request
            # Extract required fields from the JSON data
            memberName = data["memberName"]
            memberID = data["memberID"]
            nameOfInstitution = data["nameOfInstitution"]
            passportUrl = data["passportUrl"]
            memberSince = data["memberSince"]
            nameOfOrganization = data["nameOfOrganization"]
            nameOfAdmin = data["nameOfAdmin"]
            adminDesignation = data["adminDesignation"]
            currentDateTime = data["currentDateTime"]
            badgeID = data["badgeID"]

            moreInfo = data.get("moreInfo", "NIL")
            
            # Generate the PDF using the received data
            return generateMemberReference(memberName, memberID, nameOfInstitution, passportUrl, memberSince, moreInfo, 
                                            nameOfOrganization, nameOfAdmin, adminDesignation, currentDateTime, badgeID)
        except KeyError as e:
            return f"Missing required field: {e}", 400
    else:
        return "Only GET requests with JSON data are allowed", 400


@app.route('/alumni-reference', methods=["POST"])
def getDoc6():
    if request.method == "POST" and request.is_json:
        try:
            data = request.json  # Access the JSON data from the request
            # Extract required fields from the JSON data
            alumniName = data["alumniName"]
            alumniID = data["alumniID"]
            nameOfInstitution = data["nameOfInstitution"]
            alumniSince = data["alumniSince"]
            alumniCategory = data["alumniCategory"]
            nameOfAdmin = data["nameOfAdmin"]
            adminDesignation = data["adminDesignation"]
            currentDateTime = data["currentDateTime"]
            badgeID = data["badgeID"]

            moreInfo = data.get("moreInfo", "NIL")
            
            # Generate the PDF using the received data
            return generateAlumniReference(alumniName, alumniID, nameOfInstitution, alumniSince, alumniCategory, moreInfo, 
                                            nameOfAdmin, adminDesignation, currentDateTime, badgeID)
        except KeyError as e:
            return f"Missing required field: {e}", 400
    else:
        return "Only GET requests with JSON data are allowed", 400

if __name__ == '__main__':
    app.run(debug=True)
