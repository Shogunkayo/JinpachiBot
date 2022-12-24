import sys

def get_price(ovr_rating, base_rating):
    if(ovr_rating == 70):
        if(base_rating <= 300):
            return 1500
        elif(base_rating <= 399):
            return 1800
        elif(base_rating <= 449):
            return 1950
        elif(base_rating <= 474):
            return 2100
        elif(base_rating <= 499):
            return 2250
        elif(base_rating <= 524):
            return 2400
        elif(base_rating <= 549):
            return 2550
        elif(base_rating <= 594):
            return 2775
        else:
            return -1

    elif(ovr_rating == 71):
        if(base_rating <= 300):
            return 1800
        elif(base_rating <= 399):
            return 2160
        elif(base_rating <= 449):
            return 2340
        elif(base_rating <= 474):
            return 2520
        elif(base_rating <= 499):
            return 2700
        elif(base_rating <= 524):
            return 2880
        elif(base_rating <= 549):
            return 3060
        elif(base_rating <= 594):
            return 3330
        else:
            return -1
    
    elif(ovr_rating == 72):
        if(base_rating <= 300):
            return 2100
        elif(base_rating <= 399):
            return 2520
        elif(base_rating <= 449):
            return 2730
        elif(base_rating <= 474):
            return 2940
        elif(base_rating <= 499):
            return 3150
        elif(base_rating <= 524):
            return 3360
        elif(base_rating <= 549):
            return 3570
        elif(base_rating <= 594):
            return 3885
        else:
            return -1

    elif(ovr_rating == 73):
        if(base_rating <= 300):
            return 2400
        elif(base_rating <= 399):
            return 2880
        elif(base_rating <= 449):
            return 3120
        elif(base_rating <= 474):
            return 3360
        elif(base_rating <= 499):
            return 3600
        elif(base_rating <= 524):
            return 3840
        elif(base_rating <= 549):
            return 4080
        elif(base_rating <= 594):
            return 4440
        else:
            return -1

    elif(ovr_rating == 74):
        if(base_rating <= 300):
            return 2700
        elif(base_rating <= 399):
            return 3240
        elif(base_rating <= 449):
            return 3510
        elif(base_rating <= 474):
            return 3780
        elif(base_rating <= 499):
            return 4050
        elif(base_rating <= 524):
            return 4320
        elif(base_rating <= 549):
            return 4590
        elif(base_rating <= 594):
            return 4995
        else:
            return -1

    elif(ovr_rating == 75):
        if(base_rating <= 300):
            return 3000
        elif(base_rating <= 399):
            return 3600
        elif(base_rating <= 449):
            return 3900
        elif(base_rating <= 474):
            return 4200
        elif(base_rating <= 499):
            return 4500
        elif(base_rating <= 524):
            return 4800
        elif(base_rating <= 549):
            return 5100
        elif(base_rating <= 594):
            return 5550
        else:
            return -1

    elif(ovr_rating == 76):
        if(base_rating <= 300):
            return 4650
        elif(base_rating <= 399):
            return 5580
        elif(base_rating <= 449):
            return 6045
        elif(base_rating <= 474):
            return 6510
        elif(base_rating <= 499):
            return 6975
        elif(base_rating <= 524):
            return 7440
        elif(base_rating <= 549):
            return 7905
        elif(base_rating <= 594):
            return 8603
        else:
            return -1

    elif(ovr_rating == 77):
        if(base_rating <= 300):
            return 6300
        elif(base_rating <= 399):
            return 7560
        elif(base_rating <= 449):
            return 8190
        elif(base_rating <= 474):
            return 8820
        elif(base_rating <= 499):
            return 9450
        elif(base_rating <= 524):
            return 10080
        elif(base_rating <= 549):
            return 10710
        elif(base_rating <= 594):
            return 11655
        else:
            return -1
    
    elif(ovr_rating == 78):
        if(base_rating <= 300):
            return 7950
        elif(base_rating <= 399):
            return 9540
        elif(base_rating <= 449):
            return 10335
        elif(base_rating <= 474):
            return 11130
        elif(base_rating <= 499):
            return 11925
        elif(base_rating <= 524):
            return 12720
        elif(base_rating <= 549):
            return 13515
        elif(base_rating <= 594):
            return 14708
        else:
            return -1

    elif(ovr_rating == 79):
        if(base_rating <= 300):
            return 9600
        elif(base_rating <= 399):
            return 11520
        elif(base_rating <= 449):
            return 12480
        elif(base_rating <= 474):
            return 13440
        elif(base_rating <= 499):
            return 14400
        elif(base_rating <= 524):
            return 15360
        elif(base_rating <= 549):
            return 16320
        elif(base_rating <= 594):
            return 17760
        else:
            return -1
    
    elif(ovr_rating == 80):
        if(base_rating <= 300):
            return 11250
        elif(base_rating <= 399):
            return 13500
        elif(base_rating <= 449):
            return 14625
        elif(base_rating <= 474):
            return 15750
        elif(base_rating <= 499):
            return 16875
        elif(base_rating <= 524):
            return 18000
        elif(base_rating <= 549):
            return 19125
        elif(base_rating <= 594):
            return 20813
        else:
            return -1

    elif(ovr_rating == 81):
        if(base_rating <= 300):
            return 31250
        elif(base_rating <= 399):
            return 37500
        elif(base_rating <= 449):
            return 40625
        elif(base_rating <= 474):
            return 43750
        elif(base_rating <= 499):
            return 46875
        elif(base_rating <= 524):
            return 50000
        elif(base_rating <= 549):
            return 53125
        elif(base_rating <= 594):
            return 57813
        else:
            return -1
    
    elif(ovr_rating == 82):
        if(base_rating <= 300):
            return 51250
        elif(base_rating <= 399):
            return 61500
        elif(base_rating <= 449):
            return 66625
        elif(base_rating <= 474):
            return 71750
        elif(base_rating <= 499):
            return 76875
        elif(base_rating <= 524):
            return 82000
        elif(base_rating <= 549):
            return 87125
        elif(base_rating <= 594):
            return 94813
        else:
            return -1

    elif(ovr_rating == 83):
        if(base_rating <= 300):
            return 71250
        elif(base_rating <= 399):
            return 85500
        elif(base_rating <= 449):
            return 92625
        elif(base_rating <= 474):
            return 99750
        elif(base_rating <= 499):
            return 106875
        elif(base_rating <= 524):
            return 114000
        elif(base_rating <= 549):
            return 121125
        elif(base_rating <= 594):
            return 131813
        else:
            return -1

    elif(ovr_rating == 84):
        if(base_rating <= 300):
            return 91250
        elif(base_rating <= 399):
            return 109500
        elif(base_rating <= 449):
            return 118625
        elif(base_rating <= 474):
            return 127750
        elif(base_rating <= 499):
            return 136875
        elif(base_rating <= 524):
            return 146000
        elif(base_rating <= 549):
            return 155125
        elif(base_rating <= 594):
            return 168813
        else:
            return -1

    elif(ovr_rating == 85):
        if(base_rating <= 300):
            return 112500
        elif(base_rating <= 399):
            return 135000
        elif(base_rating <= 449):
            return 146250
        elif(base_rating <= 474):
            return 157500
        elif(base_rating <= 499):
            return 168750
        elif(base_rating <= 524):
            return 180000
        elif(base_rating <= 549):
            return 191250
        elif(base_rating <= 594):
            return 208125
        else:
            return -1

    elif(ovr_rating == 86):
        if(base_rating <= 300):
            return 180000
        elif(base_rating <= 399):
            return 216000
        elif(base_rating <= 449):
            return 234000
        elif(base_rating <= 474):
            return 252000
        elif(base_rating <= 499):
            return 270000
        elif(base_rating <= 524):
            return 288000
        elif(base_rating <= 549):
            return 306000
        elif(base_rating <= 594):
            return 333000
        else:
            return -1

    elif(ovr_rating == 87):
        if(base_rating <= 300):
            return 247500
        elif(base_rating <= 399):
            return 297000
        elif(base_rating <= 449):
            return 321750
        elif(base_rating <= 474):
            return 346500
        elif(base_rating <= 499):
            return 371250
        elif(base_rating <= 524):
            return 396000
        elif(base_rating <= 549):
            return 420750
        elif(base_rating <= 594):
            return 457875
        else:
            return -1
    
    elif(ovr_rating == 88):
        if(base_rating <= 300):
            return 315000
        elif(base_rating <= 399):
            return 378000
        elif(base_rating <= 449):
            return 409500
        elif(base_rating <= 474):
            return 441000
        elif(base_rating <= 499):
            return 472500
        elif(base_rating <= 524):
            return 504000
        elif(base_rating <= 549):
            return 535500
        elif(base_rating <= 594):
            return 582750
        else:
            return -1

    elif(ovr_rating == 89):
        if(base_rating <= 300):
            return 382500
        elif(base_rating <= 399):
            return 459000
        elif(base_rating <= 449):
            return 497250
        elif(base_rating <= 474):
            return 535500
        elif(base_rating <= 499):
            return 573750
        elif(base_rating <= 524):
            return 612000
        elif(base_rating <= 549):
            return 650250
        elif(base_rating <= 594):
            return 707625
        else:
            return -1

    elif(ovr_rating == 90):
        if(base_rating <= 300):
            return 450000
        elif(base_rating <= 399):
            return 540000
        elif(base_rating <= 449):
            return 585000
        elif(base_rating <= 474):
            return 630000
        elif(base_rating <= 499):
            return 675000
        elif(base_rating <= 524):
            return 720000
        elif(base_rating <= 549):
            return 765000
        elif(base_rating <= 594):
            return 832500
        else:
            return -1

    elif(ovr_rating == 91):
        if(base_rating <= 300):
            return 660000
        elif(base_rating <= 399):
            return 792000
        elif(base_rating <= 449):
            return 858000
        elif(base_rating <= 474):
            return 924000
        elif(base_rating <= 499):
            return 990000
        elif(base_rating <= 524):
            return 1056000
        elif(base_rating <= 549):
            return 1122000
        elif(base_rating <= 594):
            return 1221000
        else:
            return -1

    elif(ovr_rating == 92):
        if(base_rating <= 300):
            return 870000
        elif(base_rating <= 399):
            return 1044000
        elif(base_rating <= 449):
            return 1131000
        elif(base_rating <= 474):
            return 1218000
        elif(base_rating <= 499):
            return 1305000
        elif(base_rating <= 524):
            return 1392000
        elif(base_rating <= 549):
            return 1479000
        elif(base_rating <= 594):
            return 1609500
        else:
            return -1
    
    elif(ovr_rating == 93):
        if(base_rating <= 300):
            return 1080000
        elif(base_rating <= 399):
            return 1296000
        elif(base_rating <= 449):
            return 1404000
        elif(base_rating <= 474):
            return 1512000
        elif(base_rating <= 499):
            return 1620000
        elif(base_rating <= 524):
            return 1728000
        elif(base_rating <= 549):
            return 1836000
        elif(base_rating <= 594):
            return 1998000
        else:
            return -1

    elif(ovr_rating == 94):
        if(base_rating <= 300):
            return 1290000
        elif(base_rating <= 399):
            return 1548000
        elif(base_rating <= 449):
            return 1677000
        elif(base_rating <= 474):
            return 1806000
        elif(base_rating <= 499):
            return 1935000
        elif(base_rating <= 524):
            return 2064000
        elif(base_rating <= 549):
            return 2193000
        elif(base_rating <= 594):
            return 2386500
        else:
            return -1

    elif(ovr_rating == 95):
        if(base_rating <= 300):
            return 1500000
        elif(base_rating <= 399):
            return 1800000
        elif(base_rating <= 449):
            return 1950000
        elif(base_rating <= 474):
            return 2100000
        elif(base_rating <= 499):
            return 2250000
        elif(base_rating <= 524):
            return 2400000
        elif(base_rating <= 549):
            return 2550000
        elif(base_rating <= 594):
            return 2775000
        else:
            return -1
    
    elif(ovr_rating == 96):
        if(base_rating <= 300):
            return 1800000
        elif(base_rating <= 399):
            return 2160000
        elif(base_rating <= 449):
            return 2340000
        elif(base_rating <= 474):
            return 2520000
        elif(base_rating <= 499):
            return 2700000
        elif(base_rating <= 524):
            return 2880000
        elif(base_rating <= 549):
            return 3060000
        elif(base_rating <= 594):
            return 3330000
        else:
            return -1

    elif(ovr_rating == 97):
        if(base_rating <= 300):
            return 2100000
        elif(base_rating <= 399):
            return 2520000
        elif(base_rating <= 449):
            return 2730000
        elif(base_rating <= 474):
            return 2940000
        elif(base_rating <= 499):
            return 3150000
        elif(base_rating <= 524):
            return 3360000
        elif(base_rating <= 549):
            return 3570000
        elif(base_rating <= 594):
            return 3885000
        else:
            return -1

    elif(ovr_rating == 98):
        if(base_rating <= 300):
            return 2400000
        elif(base_rating <= 399):
            return 2880000
        elif(base_rating <= 449):
            return 3120000
        elif(base_rating <= 474):
            return 3360000
        elif(base_rating <= 499):
            return 3600000
        elif(base_rating <= 524):
            return 3840000
        elif(base_rating <= 549):
            return 4080000
        elif(base_rating <= 594):
            return 4440000
        else:
            return -1

    elif(ovr_rating == 99):
        if(base_rating <= 300):
            return 2700000
        elif(base_rating <= 399):
            return 3240000
        elif(base_rating <= 449):
            return 3510000
        elif(base_rating <= 474):
            return 3780000
        elif(base_rating <= 499):
            return 4050000
        elif(base_rating <= 524):
            return 4320000
        elif(base_rating <= 549):
            return 4590000
        elif(base_rating <= 594):
            return 4995000
        else:
            return -1
    
    else:
        return -1

if __name__ == "__main__":
    get_price(sys.argv[1], sys.argv[2])