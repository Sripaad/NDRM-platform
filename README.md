# NDRM-platform
    Natural Diasater Recovery and Management Platform 
A Platform created to help disaster affected areas recover faster and manage the resources donated.


# Ways of intraction 
1. Home page - Globe/Resource Board (essential)
2. Organisation
3. Donate / Payment Gateway (3rd party)
4. Admin panel(scrapper which shall be later automated)
5. Authority(govt entities)


## Things to do :
    NER
    Proper ML Pipeline/workflow
    Impact classification

##  locationsData.json
#   Below is a sample locations data sample parsed from scrapped data.
    {
        "Locations":
        [
            {
                "locationName" : "UniqueLocationName",
                "locationCount" : "LocationCountforLocationName",
                "locationResouces" : {
                    "water" : "count1",
                    "shelter" : "count2",
                    "medical" : "count3",
                    .......
                },
                totalResourceCount = summation(count[i]),
                "locationScore" = "locationCount + totalResourceCount"
            },
            ......
        ]
    }

# Home Page 
Globe:
1. Live Feed 
2. Needs 
3. Magnitude
4. Location

Stats(Globe/ResourceBoard) => Organisation => Donate (Payment) / Pick up location
