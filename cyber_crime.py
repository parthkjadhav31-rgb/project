print("=" * 40)
print(" CYBER CRIME INVESTIGATION")
print("=" * 40)

suspects ={
    1:"SHLOK",
    2:"DEEPAK🚩",
    3:"CHANDAN"
}

print("\ncase: Confidental File Accessed")
print("\nsuspects:")
for n, name in suspects.items():
    print(n, "-", name)

print("\nDigitel Evidence:")
print("1.login time: 11:42 PM")
print("3.Failed attempts:5")
print("4.unknown USB detected")

choice = int(input("\nselect suspect (1-3):"))

if choice == 2:
    score = 85
    print("\n login near incident time")
    print("multiple failed attempts")
    print("file accesed after login")

elif choice ==1:
    score = 30
    print("\nAnalyzing",suspects[choice],"...")
    print("\nlogin was much earlier")
    print(" no usual activity")

else:
    score = 15
    print("\nAnalyzing",suspects[choice],"...")
    print("\n no suspicious login activity")

print("\n"+"-"* 40)
print("      INVESTIGATION REPORT")
print("-" * 40)

print("suspect:",suspects[choice])
print("suspicion score:",score,"/100")

if score >=70:
    print("Risk level:HIGH⚠️")
elif score >= 40:
    print("Risk level:MEDIUM")
else:
    print("Risk level: LOW")

print("cse status: INVESTIGATION COMPLETE")
print("-" * 40) 