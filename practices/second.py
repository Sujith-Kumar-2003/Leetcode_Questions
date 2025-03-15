head = {
    "value": 11,
        "next":{
            "value":14,
            "next":{
                "value":23,
                "next":{
                    "value":12,
                    "next":None
                }
            }

        }
}

print(head['next']['next']['value'])
