# 1 se 1000 tak saare numbers print karne ka loop likho. Lekin * Agar number 3 se divisible hai toh "nav" print karvao.

    # Agar number 7 se divisible hai toh "gurukul" print karvao.
    # Agar number 21 se divisible hai toh "navgurukul" print karvao.


i=1
while i<=1000:
    if i%21==0:
        print("navgurukul",i)
    elif i%3==0:
        print("Nav",i)
    elif i%7==0:
        print("Gurukul",i)
    i=i+1    


     









# question_list = [
#     "How many continents are there?",              
#     "What is the capital of India?",            
#     "NG mei kaun se course padhaya jaata hai?"  
# ]

# options_list = [
#     ["Four", "Nine", "Seven", "Eight"],
#     ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
#     ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
# ]
# solution_list = [3, 4, 1] 

# answer_list=[
#     ["(1) Four", "(3) Seven"],
#     ["(4) Delhi", "(2) Bhopal"],
#     ["(4) Agriculture","(1) Sofware Engineering"]
# ]

# print("! 🤟🏻😊 WELCOME    TO    KON    BANEGA    CADODRPATI😊🤟🏻 !")

# i=0
# s=0
# count=0
# while i<len(question_list):
#     print(question_list[i])
#     a=0
#     b=i
#     while a<len(options_list[i]):
#             k=options_list[b][a]
#             print(a+1,k)
#             a=a+1
             
#     num1=input("DO You Want 5050 Lifeline:-:😃")
#     if num1=="yes":
#         print("50 50 lifeline")
#         if count < 1:
#             print(answer_list[b])
#             num2=int(input("Enter your answers:👉"))
#             if num2==solution_list[i] :
#                 s+=10000
#                 print("Your Answers Correct😃✌️")
#                 print("You win🥳🤘Rs/",s)  
#             else:
#                 print("😭😤Incorect answers😭😤:")  
#                 print("You can't paly again")
#                 print("You win🥳🤘Rs/",s)
#                 break
#             count+=1
           
#         else:
#             # print("You are win🥳🤘",s)
#             print("You already use lifeline:")
#             m=int(input("enter answer:"))
#             if m==solution_list[i]:
#                 print("Congres right answer☺️👇")
#                 s+=10000
#                 print("You win🥳🤘Rs/",s)
#             else:
#                 print("NO chance") 
#                 print("Your Answers is Wrong😭😤")
#                 print("You win🥳🤘Rs/",s)
#                 break
       
           
                
#     else:
#         pass 
#         k=int(input("Enter you won answer👉"))
#         if k==solution_list[i]:
#             print("Congres right answer☺️👇")
#             s+=10000
#             print("You are win✌️🥳😃Rs/",s)    
#         else:
#             print("NO chance") 
#             print("Your Answers is Wrong😭😤")
#             print("You win🥳🤘Rs/",s)
#             break
        
#     i=i+1   
         
# print("____Congrecutional you are big part of! ____KON BANEGA KARODPATI!____")     
# print("😃You are Win 😃Rs/",s)   
# print("Thank you are part of this")
           



