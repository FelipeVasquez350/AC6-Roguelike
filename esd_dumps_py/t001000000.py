# -*- coding: utf-8 -*-
def t001000000_0():
    """State 0,1"""
    StartEvent(0, 2553)
    # eventflag:6105:	Flag for skipping cutscenes when retrying 	リトライ時カットシーンスキップ用フラグ
    SetEventFlag(6105, 0)
    if GetChapter() == 4:
        """State 12"""
        # eventflag:3008:	Chapter Judgment Flag_Chapter 5 	章判定フラグ_五章中
        SetEventFlag(3008, 1)
        # eventflag:3006:	Chapter Judgment Flag_Chapter 4 	章判定フラグ_四章中
        SetEventFlag(3006, 0)
        # eventflag:3004:	Chapter Judgment Flag_Chapter 3 	章判定フラグ_三章中
        SetEventFlag(3004, 0)
        # eventflag:3000:	Chapter Judgment Flag_In Chapter 1 	章判定フラグ_一章中
        SetEventFlag(3000, 0)
        # eventflag:3002:	Chapter Judgment Flag_Chapter 2 	章判定フラグ_二章中
        SetEventFlag(3002, 0)
    elif GetChapter() == 3:
        """State 11"""
        # eventflag:3006:	Chapter Judgment Flag_Chapter 4 	章判定フラグ_四章中
        SetEventFlag(3006, 1)
        # eventflag:3004:	Chapter Judgment Flag_Chapter 3 	章判定フラグ_三章中
        SetEventFlag(3004, 0)
        # eventflag:3000:	Chapter Judgment Flag_In Chapter 1 	章判定フラグ_一章中
        SetEventFlag(3000, 0)
        # eventflag:3002:	Chapter Judgment Flag_Chapter 2 	章判定フラグ_二章中
        SetEventFlag(3002, 0)
    elif GetChapter() == 2:
        """State 10"""
        # eventflag:3004:	Chapter Judgment Flag_Chapter 3 	章判定フラグ_三章中
        SetEventFlag(3004, 1)
        # eventflag:3000:	Chapter Judgment Flag_In Chapter 1 	章判定フラグ_一章中
        SetEventFlag(3000, 0)
        # eventflag:3002:	Chapter Judgment Flag_Chapter 2 	章判定フラグ_二章中
        SetEventFlag(3002, 0)
    elif GetChapter() == 1:
        """State 9"""
        # eventflag:3002:	Chapter Judgment Flag_Chapter 2 	章判定フラグ_二章中
        SetEventFlag(3002, 1)
        # eventflag:3000:	Chapter Judgment Flag_In Chapter 1 	章判定フラグ_一章中
        SetEventFlag(3000, 0)
    else:
        """State 13"""
        # eventflag:3000:	Chapter Judgment Flag_In Chapter 1 	章判定フラグ_一章中
        SetEventFlag(3000, 1)
    """State 2,3"""
    c5_227(not DoesPlayerHaveSpEffect(5020), 1000)
    """State 19"""
    assert t001000000_x14()
    """State 4"""
    if not GetChapter():
        """State 14"""
        t001000000_x2()
        Quit()
    # mission:2050:"Attack the Watchpoint"
    elif UnkMissionComplete(2050, 1) == 1:
        """State 5"""
        Label('L0')
        if GetChapter() == 1:
            """State 15"""
            t001000000_x3()
            Quit()
        # mission:2180:"Ocean Crossing"
        elif UnkMissionComplete(2180, 1) == 1:
            """State 6"""
            if GetChapter() == 2:
                """State 16"""
                t001000000_x4()
                Quit()
            # mission:3230:"Destroy the Ice Worm"
            elif UnkMissionComplete(3230, 1) == 1:
                """State 7"""
                if GetChapter() == 3:
                    """State 17"""
                    t001000000_x5()
                    Quit()
                # mission:4035:"Reach the Coral Convergence"
                elif UnkMissionComplete(4035, 1) == 1:
                    """State 8"""
                    Label('L1')
                    assert GetChapter() == 4
                    """State 18"""
                    t001000000_x6()
                    Quit()
                # mission:4200:"Escape"
                elif UnkMissionComplete(4200, 1) == 1:
                    Goto('L1')
    # mission:2055:"Attack the Watchpoint"
    elif UnkMissionComplete(2055, 1) == 1:
        Goto('L0')

def t001000000_2():
    """State 0"""
    # mission:7970:"Destroy Artillery Installations"
    if UnkMissionComplete(7970, 1) == 1 and not GetEventFlag(9901):
        """State 1"""
        assert t001000000_3(flag1=9901)
    else:
        pass
    """State 18"""
    # mission:7920:"Grid 135 Cleanup"
    if UnkMissionComplete(7920, 1) == 1 and not GetEventFlag(9902):
        """State 2"""
        assert t001000000_3(flag1=9902)
    else:
        pass
    """State 19"""
    # mission:7900:"Destroy the Transport Helicopters"
    if UnkMissionComplete(7900, 1) == 1 and not GetEventFlag(9903):
        """State 3"""
        assert t001000000_3(flag1=9903)
    else:
        pass
    """State 4"""
    # mission:7980:"Destroy the Tester AC"
    if UnkMissionComplete(7980, 1) == 1 and not GetEventFlag(9904):
        """State 5"""
        assert t001000000_3(flag1=9904)
    else:
        pass
    """State 6"""
    # mission:2020:"Attack the Dam Complex"
    if UnkMissionComplete(2020, 1) == 1 and not GetEventFlag(9905):
        """State 7"""
        assert t001000000_3(flag1=9905)
    else:
        pass
    """State 8"""
    # mission:2080:"Destroy the Weaponized Mining Ship"
    if UnkMissionComplete(2080, 1) == 1 and not GetEventFlag(9906):
        """State 9"""
        assert t001000000_3(flag1=9906)
    else:
        pass
    """State 10"""
    # mission:2030:"Operation Wallclimber"
    if UnkMissionComplete(2030, 1) == 1 and not GetEventFlag(9907):
        """State 11"""
        assert t001000000_3(flag1=9907)
    else:
        pass
    """State 20"""
    # mission:2100:"Retrieve Combat Logs"
    if UnkMissionComplete(2100, 1) == 1 and not GetEventFlag(9908):
        """State 12"""
        assert t001000000_3(flag1=9908)
    else:
        pass
    """State 21"""
    # mission:2060:"Investigate BAWS Arsenal No. 2"
    if UnkMissionComplete(2060, 1) == 1 and not GetEventFlag(9909):
        """State 13"""
        assert t001000000_3(flag1=9909)
    else:
        pass
    """State 22"""
    # mission:2050:"Attack the Watchpoint"
    if UnkMissionComplete(2050, 1) == 1 and not GetEventFlag(9910):
        """State 14"""
        assert t001000000_3(flag1=9910)
    else:
        pass
    """State 23"""
    # mission:2120:"Infiltrate Grid 086"
    if UnkMissionComplete(2120, 1) == 1 and not GetEventFlag(9911):
        """State 15"""
        assert t001000000_3(flag1=9911)
    else:
        pass
    """State 24"""
    # mission:7960:"Eliminate the Doser Faction"
    if UnkMissionComplete(7960, 1) == 1 and not GetEventFlag(9912):
        """State 16"""
        assert t001000000_3(flag1=9912)
    else:
        pass
    """State 25"""
    # mission:2180:"Ocean Crossing"
    if UnkMissionComplete(2180, 1) == 1 and not GetEventFlag(9913):
        """State 17"""
        assert t001000000_3(flag1=9913)
    else:
        pass
    """State 26"""
    # mission:3011:"Steal the Survey Data"
    if UnkMissionComplete(3011, 1) == 1 and not GetEventFlag(9914):
        """State 27"""
        assert t001000000_3(flag1=9914)
    else:
        pass
    """State 31"""
    # mission:3030:"Attack the Refueling Base"
    if UnkMissionComplete(3030, 1) == 1 and not GetEventFlag(9915):
        """State 32"""
        assert t001000000_3(flag1=9915)
    else:
        pass
    """State 33"""
    # mission:2170:"Eliminate V.VII"
    if UnkMissionComplete(2170, 1) == 1 and not GetEventFlag(9916):
        """State 34"""
        assert t001000000_3(flag1=9916)
    else:
        pass
    """State 35"""
    # mission:3420:"Tunnel Sabotage"
    if UnkMissionComplete(3420, 1) == 1 and not GetEventFlag(9917):
        """State 36"""
        assert t001000000_3(flag1=9917)
    else:
        pass
    """State 37"""
    # mission:5100:"Survey the Uninhabited Floating City"
    if UnkMissionComplete(5100, 1) == 1 and not GetEventFlag(9918):
        """State 38"""
        assert t001000000_3(flag1=9918)
    else:
        pass
    """State 39"""
    # mission:2220:"Heavy Missile Launch Support"
    if UnkMissionComplete(2220, 1) == 1 and not GetEventFlag(9919):
        """State 40"""
        assert t001000000_3(flag1=9919)
    else:
        pass
    """State 41"""
    # mission:7990:"Eliminate the Enforcement Squads"
    if UnkMissionComplete(7990, 1) == 1 and not GetEventFlag(9920):
        """State 42"""
        assert t001000000_3(flag1=9920)
    else:
        pass
    """State 43"""
    # mission:3430:"Destroy the Special Forces Craft"
    if UnkMissionComplete(3430, 1) == 1 and not GetEventFlag(9921):
        """State 44"""
        assert t001000000_3(flag1=9921)
    else:
        pass
    """State 45"""
    # mission:3043:"Attack the Old Spaceport"
    if UnkMissionComplete(3043, 1) == 1 and not GetEventFlag(9922):
        """State 46"""
        assert t001000000_3(flag1=9922)
    else:
        pass
    """State 47"""
    # mission:3320:"Eliminate "Honest" Brute"
    if UnkMissionComplete(3320, 1) == 1 and not GetEventFlag(9923):
        """State 48"""
        assert t001000000_3(flag1=9923)
    else:
        pass
    """State 49"""
    # mission:7950:"Defend the Old Spaceport"
    if UnkMissionComplete(7950, 1) == 1 and not GetEventFlag(9924):
        """State 50"""
        assert t001000000_3(flag1=9924)
    else:
        pass
    """State 51"""
    # mission:3500:"Historic Data Recovery"
    if UnkMissionComplete(3500, 1) == 1 and not GetEventFlag(9925):
        """State 52"""
        assert t001000000_3(flag1=9925)
    else:
        pass
    """State 53"""
    # mission:3230:"Destroy the Ice Worm"
    if UnkMissionComplete(3230, 1) == 1 and not GetEventFlag(9926):
        """State 54"""
        assert t001000000_3(flag1=9926)
    else:
        pass
    """State 55"""
    # mission:4000:"Underground Exploration – Depth 1"
    if UnkMissionComplete(4000, 1) == 1 and not GetEventFlag(9927):
        """State 56"""
        assert t001000000_3(flag1=9927)
    else:
        pass
    """State 57"""
    # mission:4010:"Underground Exploration – Depth 2"
    if UnkMissionComplete(4010, 1) == 1 and not GetEventFlag(9928):
        """State 58"""
        assert t001000000_3(flag1=9928)
    else:
        pass
    """State 59"""
    # mission:4020:"Underground Exploration – Depth 3"
    if UnkMissionComplete(4020, 1) == 1 and not GetEventFlag(9929):
        """State 60"""
        assert t001000000_3(flag1=9929)
    else:
        pass
    """State 61"""
    # mission:7930:"Intercept the Redguns"
    if UnkMissionComplete(7930, 1) == 1 and not GetEventFlag(9930):
        """State 62"""
        assert t001000000_3(flag1=9930)
    else:
        pass
    """State 63"""
    # mission:4110:"Ambush the Vespers"
    if UnkMissionComplete(4110, 1) == 1 and not GetEventFlag(9931):
        """State 64"""
        assert t001000000_3(flag1=9931)
    else:
        pass
    """State 65"""
    # mission:4021:"Unknown Territory Survey"
    if UnkMissionComplete(4021, 1) == 1 and not GetEventFlag(9932):
        """State 66"""
        assert t001000000_3(flag1=9932)
    else:
        pass
    """State 67"""
    # mission:4030:"Reach the Coral Convergence"
    if UnkMissionComplete(4030, 1) == 1 and not GetEventFlag(9933):
        """State 68"""
        assert t001000000_3(flag1=9933)
    else:
        pass
    """State 69"""
    # mission:4200:"Escape"
    if UnkMissionComplete(4200, 1) == 1 and not GetEventFlag(9934):
        """State 70"""
        assert t001000000_3(flag1=9934)
    else:
        pass
    """State 71"""
    # mission:5010:"Take the Uninhabited Floating City"
    if UnkMissionComplete(5010, 1) == 1 and not GetEventFlag(9935):
        """State 72"""
        assert t001000000_3(flag1=9935)
    else:
        pass
    """State 73"""
    # mission:5020:"Intercept the Corporate Forces"
    if UnkMissionComplete(5020, 1) == 1 and not GetEventFlag(9936):
        """State 74"""
        assert t001000000_3(flag1=9936)
    else:
        pass
    """State 75"""
    # mission:5050:"Eliminate "Cinder" Carla"
    if UnkMissionComplete(5050, 1) == 1 and not GetEventFlag(9937):
        """State 76"""
        assert t001000000_3(flag1=9937)
    else:
        pass
    """State 77"""
    # mission:5040:"Breach the Kármán Line"
    if UnkMissionComplete(5040, 1) == 1 and not GetEventFlag(9938):
        """State 78"""
        assert t001000000_3(flag1=9938)
    else:
        pass
    """State 79"""
    # mission:5030:"Destroy the Drive Block"
    if UnkMissionComplete(5030, 1) == 1 and not GetEventFlag(9939):
        """State 80"""
        assert t001000000_3(flag1=9939)
    else:
        pass
    """State 81"""
    # mission:6000:"Shut Down the Closure Satellites"
    if UnkMissionComplete(6000, 1) == 1 and not GetEventFlag(9940):
        """State 82"""
        assert t001000000_3(flag1=9940)
    else:
        pass
    """State 83"""
    # mission:6010:"Bring Down the Xylem"
    if UnkMissionComplete(6010, 1) == 1 and not GetEventFlag(9941):
        """State 84"""
        assert t001000000_3(flag1=9941)
    else:
        pass
    """State 85"""
    # mission:2025:"Attack the Dam Complex"
    if UnkMissionComplete(2025, 1) == 1 and not GetEventFlag(9942):
        """State 86"""
        assert t001000000_3(flag1=9942)
    else:
        pass
    """State 87"""
    # mission:7910:"Prevent Corporate Salvage of New Tech"
    if UnkMissionComplete(7910, 1) == 1 and not GetEventFlag(9943):
        """State 88"""
        assert t001000000_3(flag1=9943)
    else:
        pass
    """State 89"""
    # mission:2240:"Defend the Dam Complex"
    if UnkMissionComplete(2240, 1) == 1 and not GetEventFlag(9944):
        """State 90"""
        assert t001000000_3(flag1=9944)
    else:
        pass
    """State 91"""
    # mission:2250:"Escort the Weaponized Mining Ship"
    if UnkMissionComplete(2250, 1) == 1 and not GetEventFlag(9945):
        """State 92"""
        assert t001000000_3(flag1=9945)
    else:
        pass
    """State 93"""
    # mission:2140:"Prisoner Rescue"
    if UnkMissionComplete(2140, 1) == 1 and not GetEventFlag(9946):
        """State 94"""
        assert t001000000_3(flag1=9946)
    else:
        pass
    """State 95"""
    # mission:2200:"Obstruct the Mandatory Inspection"
    if UnkMissionComplete(2200, 1) == 1 and not GetEventFlag(9947):
        """State 96"""
        assert t001000000_3(flag1=9947)
    else:
        pass
    """State 97"""
    # mission:2230:"Stop the Secret Data Breach"
    if UnkMissionComplete(2230, 1) == 1 and not GetEventFlag(9948):
        """State 98"""
        assert t001000000_3(flag1=9948)
    else:
        pass
    """State 99"""
    # mission:2211:"Coral Export Denial"
    if UnkMissionComplete(2211, 1) == 1 and not GetEventFlag(9949):
        """State 100"""
        assert t001000000_3(flag1=9949)
    else:
        pass
    """State 101"""
    # mission:4100:"MIA"
    if UnkMissionComplete(4100, 1) == 1 and not GetEventFlag(9950):
        """State 102"""
        assert t001000000_3(flag1=9950)
    else:
        pass
    """State 103"""
    # mission:5110:"Regain Control of the Xylem"
    if UnkMissionComplete(5110, 1) == 1 and not GetEventFlag(9951):
        """State 104"""
        assert t001000000_3(flag1=9951)
    else:
        pass
    """State 105"""
    # mission:6020:"Coral Release"
    if UnkMissionComplete(6020, 1) == 1 and not GetEventFlag(9952):
        """State 106"""
        assert t001000000_3(flag1=9952)
    else:
        pass
    """State 28"""
    SetEventFlag(9900, 0)
    if GetEventFlag(9999) == 1:
        """State 29"""
        PlayerEquipmentQuantityChange(3, 20000000, 1)
        SetEventFlag(9999, 0)
        assert t001000000_4()
    else:
        pass
    """State 30"""
    return 1

def t001000000_3(flag1=_):
    """State 0"""
    SetRNGSeed()
    ShuffleRNGSeed(5)
    if CompareRNGValue(0, 0) == 1:
        """State 1"""
        SetRNGSeed()
        ShuffleRNGSeed(4)
        if CompareRNGValue(0, 0) == 1:
            """State 2"""
            SetRNGSeed()
            ShuffleRNGSeed(4)
            if CompareRNGValue(0, 0) == 1:
                """State 3"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 4"""
                    # protector:50000000:HD-011 MELANDER
                    GiveItemDirectly(1, 50000000, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 5"""
                    # protector:51000000:BD-011 MELANDER
                    GiveItemDirectly(1, 51000000, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 6"""
                    # protector:52000000:AR-011 MELANDER
                    GiveItemDirectly(1, 52000000, 1)
                else:
                    """State 7"""
                    # protector:53000000:LG-011 MELANDER
                    GiveItemDirectly(1, 53000000, 1)
            elif CompareRNGValue(0, 1) == 1:
                """State 8"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 9"""
                    # protector:50000300:HD-012 MELANDER C3
                    GiveItemDirectly(1, 50000300, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 10"""
                    # protector:51000300:BD-012 MELANDER C3
                    GiveItemDirectly(1, 51000300, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 11"""
                    # protector:52000300:AR-012 MELANDER C3
                    GiveItemDirectly(1, 52000300, 1)
                else:
                    """State 12"""
                    # protector:53000300:LG-012 MELANDER C3
                    GiveItemDirectly(1, 53000300, 1)
            elif CompareRNGValue(0, 2) == 1:
                """State 13"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 14"""
                    # protector:50000100:HS-5000 APPETIZER
                    GiveItemDirectly(1, 50000100, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 15"""
                    # protector:51000100:CS-5000 MAIN DISH
                    GiveItemDirectly(1, 51000100, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 16"""
                    # protector:52000100:AS-5000 SALAD
                    GiveItemDirectly(1, 52000100, 1)
                else:
                    """State 17"""
                    # protector:53000100:2S-5000 DESSERT
                    GiveItemDirectly(1, 53000100, 1)
            else:
                """State 18"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 19"""
                    # protector:50000200:HD-033M VERRILL
                    GiveItemDirectly(1, 50000200, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 20"""
                    # protector:53200000:LG-033M VERRILL
                    GiveItemDirectly(1, 53200000, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 21"""
                    # protector:53300000:LG-022T BORNEMISSZA
                    GiveItemDirectly(1, 53300000, 1)
                else:
                    """State 22"""
                    # protector:50010000:DF-HD-08 TIAN-QIANG
                    GiveItemDirectly(1, 50010000, 1)
        elif CompareRNGValue(0, 1) == 1:
            """State 23"""
            SetRNGSeed()
            ShuffleRNGSeed(4)
            if CompareRNGValue(0, 0) == 1:
                """State 24"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 25"""
                    # protector:51010000:DF-BD-08 TIAN-QIANG
                    GiveItemDirectly(1, 51010000, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 26"""
                    # protector:52010000:DF-AR-08 TIAN-QIANG
                    GiveItemDirectly(1, 52010000, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 27"""
                    # protector:53010000:DF-LG-08 TIAN-QIANG
                    GiveItemDirectly(1, 53010000, 1)
                else:
                    """State 28"""
                    # protector:52010100:DF-AR-09 TIAN-LAO
                    GiveItemDirectly(1, 52010100, 1)
            elif CompareRNGValue(0, 1) == 1:
                """State 29"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 30"""
                    # protector:50020000:NACHTREIHER/44E
                    GiveItemDirectly(1, 50020000, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 31"""
                    # protector:51020000:NACHTREIHER/40E
                    GiveItemDirectly(1, 51020000, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 32"""
                    # protector:52020000:NACHTREIHER/46E
                    GiveItemDirectly(1, 52020000, 1)
                else:
                    """State 33"""
                    # protector:53020000:NACHTREIHER/42E
                    GiveItemDirectly(1, 53020000, 1)
            elif CompareRNGValue(0, 2) == 1:
                """State 34"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 35"""
                    # protector:50020100:KASUAR/44Z
                    GiveItemDirectly(1, 50020100, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 36"""
                    # protector:53120000:KASUAR/42Z
                    GiveItemDirectly(1, 53120000, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 37"""
                    # protector:50030000:VP-44S
                    GiveItemDirectly(1, 50030000, 1)
                else:
                    """State 38"""
                    # protector:51030000:VP-40S
                    GiveItemDirectly(1, 51030000, 1)
            else:
                """State 39"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 40"""
                    # protector:52030000:VP-46S
                    GiveItemDirectly(1, 52030000, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 41"""
                    # protector:53030000:VP-422
                    GiveItemDirectly(1, 53030000, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 42"""
                    # protector:50030100:VP-44D
                    GiveItemDirectly(1, 50030100, 1)
                else:
                    """State 43"""
                    # protector:52030100:VP-46D
                    GiveItemDirectly(1, 52030100, 1)
        elif CompareRNGValue(0, 2) == 1:
            """State 44"""
            SetRNGSeed()
            ShuffleRNGSeed(4)
            if CompareRNGValue(0, 0) == 1:
                """State 45"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 46"""
                    # protector:53230000:VP-424
                    GiveItemDirectly(1, 53230000, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 47"""
                    # protector:50040000:VE-44A
                    GiveItemDirectly(1, 50040000, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 48"""
                    # protector:51040000:VE-40A
                    GiveItemDirectly(1, 51040000, 1)
                else:
                    """State 49"""
                    # protector:52040000:VE-46A
                    GiveItemDirectly(1, 52040000, 1)
            elif CompareRNGValue(0, 1) == 1:
                """State 50"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 51"""
                    # protector:53040000:VE-42A
                    GiveItemDirectly(1, 53040000, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 52"""
                    # protector:50040100:VE-44B
                    GiveItemDirectly(1, 50040100, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 53"""
                    # protector:53340000:VE-42B
                    GiveItemDirectly(1, 53340000, 1)
                else:
                    """State 54"""
                    # protector:50050000:20-081 MIND ALPHA
                    GiveItemDirectly(1, 50050000, 1)
            elif CompareRNGValue(0, 2) == 1:
                """State 55"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 56"""
                    # protector:51050000:07-061 MIND ALPHA
                    GiveItemDirectly(1, 51050000, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 57"""
                    # protector:52050000:04-101 MIND ALPHA
                    GiveItemDirectly(1, 52050000, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 58"""
                    # protector:53050000:06-041 MIND ALPHA
                    GiveItemDirectly(1, 53050000, 1)
                else:
                    """State 59"""
                    # protector:50050100:20-082 MIND BETA
                    GiveItemDirectly(1, 50050100, 1)
            else:
                """State 60"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 61"""
                    # protector:53150000:06-042 MIND BETA
                    GiveItemDirectly(1, 53150000, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 62"""
                    # protector:50060000:EL-TH-10 FIRMEZA
                    GiveItemDirectly(1, 50060000, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 63"""
                    # protector:51060000:EL-TC-10 FIRMEZA
                    GiveItemDirectly(1, 51060000, 1)
                else:
                    """State 64"""
                    # protector:52060000:EL-TA-10 FIRMEZA
                    GiveItemDirectly(1, 52060000, 1)
        else:
            """State 65"""
            SetRNGSeed()
            ShuffleRNGSeed(4)
            if CompareRNGValue(0, 0) == 1:
                """State 66"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 67"""
                    # protector:53060000:EL-TL-10 FIRMEZA
                    GiveItemDirectly(1, 53060000, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 68"""
                    # protector:53360000:EL-TL-11 FORTALEZA
                    GiveItemDirectly(1, 53360000, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 69"""
                    # protector:50080000:IB-C03H: HAL 826
                    GiveItemDirectly(1, 50080000, 1)
                else:
                    """State 70"""
                    # protector:51080000:IB-C03C: HAL 826
                    GiveItemDirectly(1, 51080000, 1)
            elif CompareRNGValue(0, 1) == 1:
                """State 71"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 72"""
                    # protector:52080000:IB-C03A: HAL 826
                    GiveItemDirectly(1, 52080000, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 73"""
                    # protector:53080000:IB-C03L: HAL 826
                    GiveItemDirectly(1, 53080000, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 74"""
                    # protector:50080100:IA-C01H: EPHEMERA
                    GiveItemDirectly(1, 50080100, 1)
                else:
                    """State 75"""
                    # protector:51080100:IA-C01C: EPHEMERA
                    GiveItemDirectly(1, 51080100, 1)
            elif CompareRNGValue(0, 2) == 1:
                """State 76"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 77"""
                    # protector:52080100:IA-C01A: EPHEMERA
                    GiveItemDirectly(1, 52080100, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 78"""
                    # protector:53080100:IA-C01L: EPHEMERA
                    GiveItemDirectly(1, 53080100, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 79"""
                    # protector:50070200:AH-J-124 BASHO
                    GiveItemDirectly(1, 50070200, 1)
                else:
                    """State 80"""
                    # protector:51070200:AC-J-120 BASHO
                    GiveItemDirectly(1, 51070200, 1)
            else:
                """State 81"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 82"""
                    # protector:52070200:AA-J-123 BASHO
                    GiveItemDirectly(1, 52070200, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 83"""
                    # protector:53070200:AL-J-121 BASHO
                    GiveItemDirectly(1, 53070200, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 84"""
                    # protector:50900000:AH-J-124/RC JAILBREAK
                    GiveItemDirectly(1, 50900000, 1)
                else:
                    """State 85"""
                    # protector:51900000:AC-J-120/RC JAILBREAK
                    GiveItemDirectly(1, 51900000, 1)
    elif CompareRNGValue(0, 1) == 1:
        """State 86"""
        SetRNGSeed()
        ShuffleRNGSeed(4)
        if CompareRNGValue(0, 0) == 1:
            """State 87"""
            SetRNGSeed()
            ShuffleRNGSeed(4)
            if CompareRNGValue(0, 0) == 1:
                """State 88"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 89"""
                    # protector:52900000:AA-J-123/RC JAILBREAK
                    GiveItemDirectly(1, 52900000, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 90"""
                    # protector:53900000:AL-J-121/RC JAILBREAK
                    GiveItemDirectly(1, 53900000, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 91"""
                    # protector:50070300:HC-3000 WRECKER
                    GiveItemDirectly(1, 50070300, 1)
                else:
                    """State 92"""
                    # protector:51070300:CC-3000 WRECKER
                    GiveItemDirectly(1, 51070300, 1)
            elif CompareRNGValue(0, 1) == 1:
                """State 93"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 94"""
                    # protector:52070300:AC-3000 WRECKER
                    GiveItemDirectly(1, 52070300, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 95"""
                    # protector:53070300:2C-3000 WRECKER
                    GiveItemDirectly(1, 53070300, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 96"""
                    # protector:50070400:HC-2000 FINDER EYE
                    GiveItemDirectly(1, 50070400, 1)
                else:
                    """State 97"""
                    # protector:51070400:CC-2000 ORBITER
                    GiveItemDirectly(1, 51070400, 1)
            elif CompareRNGValue(0, 2) == 1:
                """State 98"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 99"""
                    # protector:52070400:AC-2000 TOOL ARM
                    GiveItemDirectly(1, 52070400, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 100"""
                    # protector:53070400:2C-2000 CRAWLER
                    GiveItemDirectly(1, 53070400, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 101"""
                    # protector:50070600:HC-2000/BC SHADE EYE
                    GiveItemDirectly(1, 50070600, 1)
                else:
                    """State 102"""
                    # protector:53170400:RC-2000 SPRING CHICKEN
                    GiveItemDirectly(1, 53170400, 1)
            else:
                """State 103"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 104"""
                    # protector:50080200:EL-PH-00 ALBA
                    GiveItemDirectly(1, 50080200, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 105"""
                    # protector:51080200:EL-PC-00 ALBA
                    GiveItemDirectly(1, 51080200, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 106"""
                    # protector:52080200:EL-PA-00 ALBA
                    GiveItemDirectly(1, 52080200, 1)
                else:
                    """State 107"""
                    # protector:53080200:EL-PL-00 ALBA
                    GiveItemDirectly(1, 53080200, 1)
        elif CompareRNGValue(0, 1) == 1:
            """State 108"""
            SetRNGSeed()
            ShuffleRNGSeed(4)
            if CompareRNGValue(0, 0) == 1:
                """State 109"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 110"""
                    # protector:50080300:LAMMERGEIER/44F
                    GiveItemDirectly(1, 50080300, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 111"""
                    # protector:51080300:LAMMERGEIER/40F
                    GiveItemDirectly(1, 51080300, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 112"""
                    # protector:52080300:LAMMERGEIER/46F
                    GiveItemDirectly(1, 52080300, 1)
                else:
                    """State 113"""
                    # protector:53280300:LAMMERGEIER/42F
                    GiveItemDirectly(1, 53280300, 1)
            elif CompareRNGValue(0, 1) == 1:
                """State 114"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 115"""
                    # booster:60000000:BST-G2/P04
                    GiveItemDirectly(6, 60000000, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 116"""
                    # booster:60010000:BC-0600 12345
                    GiveItemDirectly(6, 60010000, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 117"""
                    # booster:60020000:ALULA/21E
                    GiveItemDirectly(6, 60020000, 1)
                else:
                    """State 118"""
                    # booster:60030000:FLUEGEL/21Z
                    GiveItemDirectly(6, 60030000, 1)
            elif CompareRNGValue(0, 2) == 1:
                """State 119"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 120"""
                    # booster:60040000:BUERZEL/21D
                    GiveItemDirectly(6, 60040000, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 121"""
                    # booster:60050000:BST-G2/P06SPD
                    GiveItemDirectly(6, 60050000, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 122"""
                    # booster:60060000:BC-0200 GRIDWALKER
                    GiveItemDirectly(6, 60060000, 1)
                else:
                    """State 123"""
                    # booster:60070000:IB-C03B: NGI 001
                    GiveItemDirectly(6, 60070000, 1)
            else:
                """State 124"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 125"""
                    # booster:60070100:IA-C01B: GILLS
                    GiveItemDirectly(6, 60070100, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 126"""
                    # booster:60070200:AB-J-137 KIKAKU
                    GiveItemDirectly(6, 60070200, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 127"""
                    # booster:60070300:BC-0400 MULE
                    GiveItemDirectly(6, 60070300, 1)
                else:
                    """State 128"""
                    # booster:60070400:BST-G1/P10
                    GiveItemDirectly(6, 60070400, 1)
        elif CompareRNGValue(0, 2) == 1:
            """State 129"""
            SetRNGSeed()
            ShuffleRNGSeed(4)
            if CompareRNGValue(0, 0) == 1:
                """State 130"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 131"""
                    # fcs:70000000:FCS-G1/P01
                    GiveItemDirectly(7, 70000000, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 132"""
                    # fcs:70010000:FCS-G2/P05
                    GiveItemDirectly(7, 70010000, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 133"""
                    # fcs:70010100:FCS-G2/P10SLT
                    GiveItemDirectly(7, 70010100, 1)
                else:
                    """State 134"""
                    # fcs:70010200:FCS-G2/P12SML
                    GiveItemDirectly(7, 70010200, 1)
            elif CompareRNGValue(0, 1) == 1:
                """State 135"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 136"""
                    # fcs:70010300:FC-006 ABBOT
                    GiveItemDirectly(7, 70010300, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 137"""
                    # fcs:70010400:FC-008 TALBOT
                    GiveItemDirectly(7, 70010400, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 138"""
                    # fcs:70020000:VE-21A
                    GiveItemDirectly(7, 70020000, 1)
                else:
                    """State 139"""
                    # fcs:70020100:VE-21B
                    GiveItemDirectly(7, 70020100, 1)
            elif CompareRNGValue(0, 2) == 1:
                """State 140"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 141"""
                    # fcs:70030000:IA-C01F: OCELLUS
                    GiveItemDirectly(7, 70030000, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 142"""
                    # fcs:70030100:IB-C03F: WLT 001
                    GiveItemDirectly(7, 70030100, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 143"""
                    # generator:65000000:AG-J-098 JOSO
                    GiveItemDirectly(5, 65000000, 1)
                else:
                    """State 144"""
                    # generator:65010000:DF-GN-02 LING-TAI
                    GiveItemDirectly(5, 65010000, 1)
            else:
                """State 145"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 146"""
                    # generator:65010100:DF-GN-06 MING-TANG
                    GiveItemDirectly(5, 65010100, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 147"""
                    # generator:65040000:DF-GN-08 SAN-TAI
                    GiveItemDirectly(5, 65040000, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 148"""
                    # generator:65010200:VP-20S
                    GiveItemDirectly(5, 65010200, 1)
                else:
                    """State 149"""
                    # generator:65010300:VP-20C
                    GiveItemDirectly(5, 65010300, 1)
        else:
            """State 150"""
            SetRNGSeed()
            ShuffleRNGSeed(4)
            if CompareRNGValue(0, 0) == 1:
                """State 151"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 152"""
                    # generator:65040100:VP-20D
                    GiveItemDirectly(5, 65040100, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 153"""
                    # generator:65010400:AG-E-013 YABA
                    GiveItemDirectly(5, 65010400, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 154"""
                    # generator:65040200:AG-T-005 HOKUSHI
                    GiveItemDirectly(5, 65040200, 1)
                else:
                    """State 155"""
                    # generator:65020000:VE-20A
                    GiveItemDirectly(5, 65020000, 1)
            elif CompareRNGValue(0, 1) == 1:
                """State 156"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 157"""
                    # generator:65020100:VE-20B
                    GiveItemDirectly(5, 65020100, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 158"""
                    # generator:65040300:VE-20C
                    GiveItemDirectly(5, 65040300, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 159"""
                    # generator:65030000:IA-C01G: AORTA
                    GiveItemDirectly(5, 65030000, 1)
                else:
                    """State 160"""
                    # generator:65030100:IB-C03G: NGI 000
                    GiveItemDirectly(5, 65030100, 1)
            elif CompareRNGValue(0, 2) == 1:
                """State 161"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 162"""
                    # weapon:10060000:DF-GR-07 GOU-CHEN
                    GiveItemDirectly(0, 10060000, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 163"""
                    # weapon:15060000:DF-GR-07 GOU-CHEN
                    GiveItemDirectly(0, 15060000, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 164"""
                    # weapon:10060100:DIZZY
                    GiveItemDirectly(0, 10060100, 1)
                else:
                    """State 165"""
                    # weapon:15060100:DIZZY
                    GiveItemDirectly(0, 15060100, 1)
            else:
                """State 166"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 167"""
                    # weapon:10040000:LITTLE GEM
                    GiveItemDirectly(0, 10040000, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 168"""
                    # weapon:15040000:LITTLE GEM
                    GiveItemDirectly(0, 15040000, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 169"""
                    # weapon:10040100:MAJESTIC
                    GiveItemDirectly(0, 10040100, 1)
                else:
                    """State 170"""
                    # weapon:15040100:MAJESTIC
                    GiveItemDirectly(0, 15040100, 1)
    elif CompareRNGValue(0, 2) == 1:
        """State 171"""
        SetRNGSeed()
        ShuffleRNGSeed(4)
        if CompareRNGValue(0, 0) == 1:
            """State 172"""
            SetRNGSeed()
            ShuffleRNGSeed(4)
            if CompareRNGValue(0, 0) == 1:
                """State 173"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 174"""
                    # weapon:10040200:DF-BA-06 XUAN-GE
                    GiveItemDirectly(0, 10040200, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 175"""
                    # weapon:15040200:DF-BA-06 XUAN-GE
                    GiveItemDirectly(0, 15040200, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 176"""
                    # weapon:10050000:WR-0777 SWEET SIXTEEN
                    GiveItemDirectly(0, 10050000, 1)
                else:
                    """State 177"""
                    # weapon:15050000:WR-0777 SWEET SIXTEEN
                    GiveItemDirectly(0, 15050000, 1)
            elif CompareRNGValue(0, 1) == 1:
                """State 178"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 179"""
                    # weapon:10050100:SG-026 HALDEMAN
                    GiveItemDirectly(0, 10050100, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 180"""
                    # weapon:15050100:SG-026 HALDEMAN
                    GiveItemDirectly(0, 15050100, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 181"""
                    # weapon:10050200:SG-027 ZIMMERMAN
                    GiveItemDirectly(0, 10050200, 1)
                else:
                    """State 182"""
                    # weapon:15050200:SG-027 ZIMMERMAN
                    GiveItemDirectly(0, 15050200, 1)
            elif CompareRNGValue(0, 2) == 1:
                """State 183"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 184"""
                    # weapon:10000000:MA-J-200 RANSETSU-RF
                    GiveItemDirectly(0, 10000000, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 185"""
                    # weapon:15000000:MA-J-200 RANSETSU-RF
                    GiveItemDirectly(0, 15000000, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 186"""
                    # weapon:10000100:LR-036 CURTIS
                    GiveItemDirectly(0, 10000100, 1)
                else:
                    """State 187"""
                    # weapon:15000100:LR-036 CURTIS
                    GiveItemDirectly(0, 15000100, 1)
            else:
                """State 188"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 189"""
                    # weapon:10000200:LR-037 HARRIS
                    GiveItemDirectly(0, 10000200, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 190"""
                    # weapon:15000200:LR-037 HARRIS
                    GiveItemDirectly(0, 15000200, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 191"""
                    # weapon:10010000:MA-J-201 RANSETSU-AR
                    GiveItemDirectly(0, 10010000, 1)
                else:
                    """State 192"""
                    # weapon:15010000:MA-J-201 RANSETSU-AR
                    GiveItemDirectly(0, 15010000, 1)
        elif CompareRNGValue(0, 1) == 1:
            """State 193"""
            SetRNGSeed()
            ShuffleRNGSeed(4)
            if CompareRNGValue(0, 0) == 1:
                """State 194"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 195"""
                    # weapon:10010100:RF-024 TURNER
                    GiveItemDirectly(0, 10010100, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 196"""
                    # weapon:15010100:RF-024 TURNER
                    GiveItemDirectly(0, 15010100, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 197"""
                    # weapon:10010200:RF-025 SCUDDER
                    GiveItemDirectly(0, 10010200, 1)
                else:
                    """State 198"""
                    # weapon:15010200:RF-025 SCUDDER
                    GiveItemDirectly(0, 15010200, 1)
            elif CompareRNGValue(0, 1) == 1:
                """State 199"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 200"""
                    # weapon:10020000:MA-E-210 ETSUJIN
                    GiveItemDirectly(0, 10020000, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 201"""
                    # weapon:15020000:MA-E-210 ETSUJIN
                    GiveItemDirectly(0, 15020000, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 202"""
                    # weapon:10020100:MG-014 LUDLOW
                    GiveItemDirectly(0, 10020100, 1)
                else:
                    """State 203"""
                    # weapon:15020100:MG-014 LUDLOW
                    GiveItemDirectly(0, 15020100, 1)
            elif CompareRNGValue(0, 2) == 1:
                """State 204"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 205"""
                    # weapon:10020200:DF-MG-02 CHANG-CHEN
                    GiveItemDirectly(0, 10020200, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 206"""
                    # weapon:15020200:DF-MG-02 CHANG-CHEN
                    GiveItemDirectly(0, 15020200, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 207"""
                    # weapon:10020300:WR-0555 ATTACHE
                    GiveItemDirectly(0, 10020300, 1)
                else:
                    """State 208"""
                    # weapon:15020300:WR-0555 ATTACHE
                    GiveItemDirectly(0, 15020300, 1)
            else:
                """State 209"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 210"""
                    # weapon:10030000:DF-GA-08 HU-BEN
                    GiveItemDirectly(0, 10030000, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 211"""
                    # weapon:15030000:DF-GA-08 HU-BEN
                    GiveItemDirectly(0, 15030000, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 212"""
                    # weapon:10070000:EL-PW-00 VIENTO
                    GiveItemDirectly(0, 10070000, 1)
                else:
                    """State 213"""
                    # weapon:15070000:EL-PW-00 VIENTO
                    GiveItemDirectly(0, 15070000, 1)
        elif CompareRNGValue(0, 2) == 1:
            """State 214"""
            SetRNGSeed()
            ShuffleRNGSeed(4)
            if CompareRNGValue(0, 0) == 1:
                """State 215"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 216"""
                    # weapon:10070100:MA-E-211 SAMPU
                    GiveItemDirectly(0, 10070100, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 217"""
                    # weapon:15070100:MA-E-211 SAMPU
                    GiveItemDirectly(0, 15070100, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 218"""
                    # weapon:10070200:HG-003 COQUILLETT
                    GiveItemDirectly(0, 10070200, 1)
                else:
                    """State 219"""
                    # weapon:15070200:HG-003 COQUILLETT
                    GiveItemDirectly(0, 15070200, 1)
            elif CompareRNGValue(0, 1) == 1:
                """State 220"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 221"""
                    # weapon:10070300:HG-004 DUCKETT
                    GiveItemDirectly(0, 10070300, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 222"""
                    # weapon:15070300:HG-004 DUCKETT
                    GiveItemDirectly(0, 15070300, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 223"""
                    # weapon:10080000:MA-T-223 KYORIKU
                    GiveItemDirectly(0, 10080000, 1)
                else:
                    """State 224"""
                    # weapon:15080000:MA-T-223 KYORIKU
                    GiveItemDirectly(0, 15080000, 1)
            elif CompareRNGValue(0, 2) == 1:
                """State 225"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 226"""
                    # weapon:10080100:MA-T-222 KYORAI
                    GiveItemDirectly(0, 10080100, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 227"""
                    # weapon:15080100:MA-T-222 KYORAI
                    GiveItemDirectly(0, 15080100, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 228"""
                    # weapon:10080200:WS-1200 THERAPIST
                    GiveItemDirectly(0, 10080200, 1)
                else:
                    """State 229"""
                    # weapon:15080200:WS-1200 THERAPIST
                    GiveItemDirectly(0, 15080200, 1)
            else:
                """State 230"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 231"""
                    # weapon:10090000:HML-G2/P19MLT-04
                    GiveItemDirectly(0, 10090000, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 232"""
                    # weapon:15090000:HML-G2/P19MLT-04
                    GiveItemDirectly(0, 15090000, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 233"""
                    # weapon:10090100:HML-G3/P08SPL-06
                    GiveItemDirectly(0, 10090100, 1)
                else:
                    """State 234"""
                    # weapon:15090100:HML-G3/P08SPL-06
                    GiveItemDirectly(0, 15090100, 1)
        else:
            """State 235"""
            SetRNGSeed()
            ShuffleRNGSeed(4)
            if CompareRNGValue(0, 0) == 1:
                """State 236"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 237"""
                    # weapon:10100000:IRIDIUM
                    GiveItemDirectly(0, 10100000, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 238"""
                    # weapon:15100000:IRIDIUM
                    GiveItemDirectly(0, 15100000, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 239"""
                    # weapon:10120100:44-142 KRSV
                    GiveItemDirectly(0, 10120100, 1)
                else:
                    """State 240"""
                    # weapon:15120100:44-142 KRSV
                    GiveItemDirectly(0, 15120100, 1)
            elif CompareRNGValue(0, 1) == 1:
                """State 241"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 242"""
                    # weapon:10120000:Vvc-760PR
                    GiveItemDirectly(0, 10120000, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 243"""
                    # weapon:15120000:Vvc-760PR
                    GiveItemDirectly(0, 15120000, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 244"""
                    # weapon:10140000:VE-66LRB
                    GiveItemDirectly(0, 10140000, 1)
                else:
                    """State 245"""
                    # weapon:15140000:VE-66LRB
                    GiveItemDirectly(0, 15140000, 1)
            elif CompareRNGValue(0, 2) == 1:
                """State 246"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 247"""
                    # weapon:10150000:WUERGER/66E
                    GiveItemDirectly(0, 10150000, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 248"""
                    # weapon:15150000:WUERGER/66E
                    GiveItemDirectly(0, 15150000, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 249"""
                    # weapon:10150100:VP-66LS
                    GiveItemDirectly(0, 10150100, 1)
                else:
                    """State 250"""
                    # weapon:15150100:VP-66LS
                    GiveItemDirectly(0, 15150100, 1)
            else:
                """State 251"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 252"""
                    # weapon:10150200:IA-C01W1: NEBULA
                    GiveItemDirectly(0, 10150200, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 253"""
                    # weapon:15150200:IA-C01W1: NEBULA
                    GiveItemDirectly(0, 15150200, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 254"""
                    # weapon:10150300:IA-C01W6: NB-REDSHIFT
                    GiveItemDirectly(0, 10150300, 1)
                else:
                    """State 255"""
                    # weapon:15150300:IA-C01W6: NB-REDSHIFT
                    GiveItemDirectly(0, 15150300, 1)
    elif CompareRNGValue(0, 3) == 1:
        """State 256"""
        SetRNGSeed()
        ShuffleRNGSeed(4)
        if CompareRNGValue(0, 0) == 1:
            """State 257"""
            SetRNGSeed()
            ShuffleRNGSeed(4)
            if CompareRNGValue(0, 0) == 1:
                """State 258"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 259"""
                    # weapon:10110000:VP-66LH
                    GiveItemDirectly(0, 10110000, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 260"""
                    # weapon:15110000:VP-66LH
                    GiveItemDirectly(0, 15110000, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 261"""
                    # weapon:10110100:VP-66LR
                    GiveItemDirectly(0, 10110100, 1)
                else:
                    """State 262"""
                    # weapon:15110100:VP-66LR
                    GiveItemDirectly(0, 15110100, 1)
            elif CompareRNGValue(0, 1) == 1:
                """State 263"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 264"""
                    # weapon:10110200:IB-C03W1: WLT 011
                    GiveItemDirectly(0, 10110200, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 265"""
                    # weapon:15110200:IB-C03W1: WLT 011
                    GiveItemDirectly(0, 15110200, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 266"""
                    # weapon:10110300:VE-66LRA
                    GiveItemDirectly(0, 10110300, 1)
                else:
                    """State 267"""
                    # weapon:15110300:VE-66LRA
                    GiveItemDirectly(0, 15110300, 1)
            elif CompareRNGValue(0, 2) == 1:
                """State 268"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 269"""
                    # weapon:10130000:HI-16: GU-Q1
                    GiveItemDirectly(0, 10130000, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 270"""
                    # weapon:15130000:HI-16: GU-Q1
                    GiveItemDirectly(0, 15130000, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 271"""
                    # weapon:10130100:HI-18: GU-A2
                    GiveItemDirectly(0, 10130100, 1)
                else:
                    """State 272"""
                    # weapon:15130100:HI-18: GU-A2
                    GiveItemDirectly(0, 15130100, 1)
            else:
                """State 273"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 274"""
                    # weapon:10160000:WB-0000 BAD COOK
                    GiveItemDirectly(0, 10160000, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 275"""
                    # weapon:15160000:WB-0000 BAD COOK
                    GiveItemDirectly(0, 15160000, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 276"""
                    # weapon:10170000:44-141 JVLN ALPHA
                    GiveItemDirectly(0, 10170000, 1)
                else:
                    """State 277"""
                    # weapon:15170000:44-141 JVLN ALPHA
                    GiveItemDirectly(0, 15170000, 1)
        elif CompareRNGValue(0, 1) == 1:
            """State 278"""
            SetRNGSeed()
            ShuffleRNGSeed(4)
            if CompareRNGValue(0, 0) == 1:
                """State 279"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 280"""
                    # weapon:10180000:VP-66EG
                    GiveItemDirectly(0, 10180000, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 281"""
                    # weapon:15180000:VP-66EG
                    GiveItemDirectly(0, 15180000, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 282"""
                    # weapon:10190000:WS-5000 APERITIF
                    GiveItemDirectly(0, 10190000, 1)
                else:
                    """State 283"""
                    # weapon:15190000:WS-5000 APERITIF
                    GiveItemDirectly(0, 15190000, 1)
            elif CompareRNGValue(0, 1) == 1:
                """State 284"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 285"""
                    # weapon:10300000:PFAU/66D
                    GiveItemDirectly(0, 10300000, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 286"""
                    # weapon:15300000:PFAU/66D
                    GiveItemDirectly(0, 15300000, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 287"""
                    # weapon:20080000:PB-033M ASHMEAD
                    GiveItemDirectly(0, 20080000, 1)
                else:
                    """State 288"""
                    # weapon:20010000:HI-32: BU-TT/A
                    GiveItemDirectly(0, 20010000, 1)
            elif CompareRNGValue(0, 2) == 1:
                """State 289"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 290"""
                    # weapon:20020000:Vvc-770LB
                    GiveItemDirectly(0, 20020000, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 291"""
                    # weapon:20000100:IB-C03W2: WLT 101
                    GiveItemDirectly(0, 20000100, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 292"""
                    # weapon:20040000:VP-67LD
                    GiveItemDirectly(0, 20040000, 1)
                else:
                    """State 293"""
                    # weapon:20000200:IA-C01W2: MOONLIGHT
                    GiveItemDirectly(0, 20000200, 1)
            else:
                """State 294"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 295"""
                    # weapon:20000300:IA-C01W7: ML-REDSHIFT
                    GiveItemDirectly(0, 20000300, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 296"""
                    # weapon:20030000:Vvc-774LS
                    GiveItemDirectly(0, 20030000, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 297"""
                    # weapon:20100000:DF-ET-09 TAI-YANG-SHOU
                    GiveItemDirectly(0, 20100000, 1)
                else:
                    """State 298"""
                    # weapon:20050000:VE-67LLA
                    GiveItemDirectly(0, 20050000, 1)
        elif CompareRNGValue(0, 2) == 1:
            """State 299"""
            SetRNGSeed()
            ShuffleRNGSeed(4)
            if CompareRNGValue(0, 0) == 1:
                """State 300"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 301"""
                    # weapon:20090000:VP-67EB
                    GiveItemDirectly(0, 20090000, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 302"""
                    # weapon:20060000:WB-0010 DOUBLE TROUBLE
                    GiveItemDirectly(0, 20060000, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 303"""
                    # weapon:20070000:44-143 HMMR
                    GiveItemDirectly(0, 20070000, 1)
                else:
                    """State 304"""
                    # weapon:30210000:EARSHOT
                    GiveItemDirectly(0, 30210000, 1)
            elif CompareRNGValue(0, 1) == 1:
                """State 305"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 306"""
                    # weapon:35210000:EARSHOT
                    GiveItemDirectly(0, 35210000, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 307"""
                    # weapon:30200000:SB-033M MORLEY
                    GiveItemDirectly(0, 30200000, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 308"""
                    # weapon:35200000:SB-033M MORLEY
                    GiveItemDirectly(0, 35200000, 1)
                else:
                    """State 309"""
                    # weapon:30000000:Vvc-703PM
                    GiveItemDirectly(0, 30000000, 1)
            elif CompareRNGValue(0, 2) == 1:
                """State 310"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 311"""
                    # weapon:35000000:Vvc-703PM
                    GiveItemDirectly(0, 35000000, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 312"""
                    # weapon:30000200:Vvc-706PM
                    GiveItemDirectly(0, 30000200, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 313"""
                    # weapon:35000200:Vvc-706PM
                    GiveItemDirectly(0, 35000200, 1)
                else:
                    """State 314"""
                    # weapon:30000100:Vvc-70VPM
                    GiveItemDirectly(0, 30000100, 1)
            else:
                """State 315"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 316"""
                    # weapon:35000100:Vvc-70VPM
                    GiveItemDirectly(0, 35000100, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 317"""
                    # weapon:30010000:BML-G3/P05ACT-02
                    GiveItemDirectly(0, 30010000, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 318"""
                    # weapon:35010000:BML-G3/P05ACT-02
                    GiveItemDirectly(0, 35010000, 1)
                else:
                    """State 319"""
                    # weapon:30010100:BML-G3/P04ACT-01
                    GiveItemDirectly(0, 30010100, 1)
        else:
            """State 320"""
            SetRNGSeed()
            ShuffleRNGSeed(4)
            if CompareRNGValue(0, 0) == 1:
                """State 321"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 322"""
                    # weapon:35010100:BML-G3/P04ACT-01
                    GiveItemDirectly(0, 35010100, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 323"""
                    # weapon:30030000:IB-C03W3: NGI 006
                    GiveItemDirectly(0, 30030000, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 324"""
                    # weapon:35030000:IB-C03W3: NGI 006
                    GiveItemDirectly(0, 35030000, 1)
                else:
                    """State 325"""
                    # weapon:30040000:BML-G1/P07VTC-12
                    GiveItemDirectly(0, 30040000, 1)
            elif CompareRNGValue(0, 1) == 1:
                """State 326"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 327"""
                    # weapon:35040000:BML-G1/P07VTC-12
                    GiveItemDirectly(0, 35040000, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 328"""
                    # weapon:30040100:BML-G1/P03VTC-08
                    GiveItemDirectly(0, 30040100, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 329"""
                    # weapon:35040100:BML-G1/P03VTC-08
                    GiveItemDirectly(0, 35040100, 1)
                else:
                    """State 330"""
                    # weapon:30040200:BML-G1/P01VTC-04
                    GiveItemDirectly(0, 30040200, 1)
            elif CompareRNGValue(0, 2) == 1:
                """State 331"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 332"""
                    # weapon:35040200:BML-G1/P01VTC-04
                    GiveItemDirectly(0, 35040200, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 333"""
                    # weapon:30050000:45-091 JVLN BETA
                    GiveItemDirectly(0, 30050000, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 334"""
                    # weapon:35050000:45-091 JVLN BETA
                    GiveItemDirectly(0, 35050000, 1)
                else:
                    """State 335"""
                    # weapon:30070000:WS-5001 SOUP
                    GiveItemDirectly(0, 30070000, 1)
            else:
                """State 336"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 337"""
                    # weapon:35070000:WS-5001 SOUP
                    GiveItemDirectly(0, 35070000, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 338"""
                    # weapon:30020000:BML-G2/P03MLT-06
                    GiveItemDirectly(0, 30020000, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 339"""
                    # weapon:35020000:BML-G2/P03MLT-06
                    GiveItemDirectly(0, 35020000, 1)
                else:
                    """State 340"""
                    # weapon:30020100:BML-G1/P20MLT-04
                    GiveItemDirectly(0, 30020100, 1)
    else:
        """State 341"""
        SetRNGSeed()
        ShuffleRNGSeed(4)
        if CompareRNGValue(0, 0) == 1:
            """State 342"""
            SetRNGSeed()
            ShuffleRNGSeed(4)
            if CompareRNGValue(0, 0) == 1:
                """State 343"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 344"""
                    # weapon:35020100:BML-G1/P20MLT-04
                    GiveItemDirectly(0, 35020100, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 345"""
                    # weapon:30020200:BML-G2/P05MLT-10
                    GiveItemDirectly(0, 30020200, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 346"""
                    # weapon:35020200:BML-G2/P05MLT-10
                    GiveItemDirectly(0, 35020200, 1)
                else:
                    """State 347"""
                    # weapon:30080000:BML-G1/P32DUO-03
                    GiveItemDirectly(0, 30080000, 1)
            elif CompareRNGValue(0, 1) == 1:
                """State 348"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 349"""
                    # weapon:35080000:BML-G1/P32DUO-03
                    GiveItemDirectly(0, 35080000, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 350"""
                    # weapon:30080100:BML-G2/P08DUO-03
                    GiveItemDirectly(0, 30080100, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 351"""
                    # weapon:35080100:BML-G2/P08DUO-03
                    GiveItemDirectly(0, 35080100, 1)
                else:
                    """State 352"""
                    # weapon:30090200:BML-G2/P17SPL-16
                    GiveItemDirectly(0, 30090200, 1)
            elif CompareRNGValue(0, 2) == 1:
                """State 353"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 354"""
                    # weapon:35090200:BML-G2/P17SPL-16
                    GiveItemDirectly(0, 35090200, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 355"""
                    # weapon:30080200:BML-G1/P31DUO-02
                    GiveItemDirectly(0, 30080200, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 356"""
                    # weapon:35080200:BML-G1/P31DUO-02
                    GiveItemDirectly(0, 35080200, 1)
                else:
                    """State 357"""
                    # weapon:30090000:BML-G2/P19SPL-12
                    GiveItemDirectly(0, 30090000, 1)
            else:
                """State 358"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 359"""
                    # weapon:35090000:BML-G2/P19SPL-12
                    GiveItemDirectly(0, 35090000, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 360"""
                    # weapon:30090100:BML-G2/P16SPL-08
                    GiveItemDirectly(0, 30090100, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 361"""
                    # weapon:35090100:BML-G2/P16SPL-08
                    GiveItemDirectly(0, 35090100, 1)
                else:
                    """State 362"""
                    # weapon:30120000:BML-G1/P29CNT
                    GiveItemDirectly(0, 30120000, 1)
        elif CompareRNGValue(0, 1) == 1:
            """State 363"""
            SetRNGSeed()
            ShuffleRNGSeed(4)
            if CompareRNGValue(0, 0) == 1:
                """State 364"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 365"""
                    # weapon:35120000:BML-G1/P29CNT
                    GiveItemDirectly(0, 35120000, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 366"""
                    # weapon:30110000:EL-PW-01 TRUENO
                    GiveItemDirectly(0, 30110000, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 367"""
                    # weapon:35110000:EL-PW-01 TRUENO
                    GiveItemDirectly(0, 35110000, 1)
                else:
                    """State 368"""
                    # weapon:30130000:WR-0999 DELIVERY BOY
                    GiveItemDirectly(0, 30130000, 1)
            elif CompareRNGValue(0, 1) == 1:
                """State 369"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 370"""
                    # weapon:35130000:WR-0999 DELIVERY BOY
                    GiveItemDirectly(0, 35130000, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 371"""
                    # weapon:30350100:IA-C01W3: AURORA
                    GiveItemDirectly(0, 30350100, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 372"""
                    # weapon:35350100:IA-C01W3: AURORA
                    GiveItemDirectly(0, 35350100, 1)
                else:
                    """State 373"""
                    # weapon:30100000:SONGBIRDS
                    GiveItemDirectly(0, 30100000, 1)
            elif CompareRNGValue(0, 2) == 1:
                """State 374"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 375"""
                    # weapon:35100000:SONGBIRDS
                    GiveItemDirectly(0, 35100000, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 376"""
                    # weapon:30230000:FASAN/60E
                    GiveItemDirectly(0, 30230000, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 377"""
                    # weapon:35230000:FASAN/60E
                    GiveItemDirectly(0, 35230000, 1)
                else:
                    """State 378"""
                    # weapon:30250000:VP-60LCS
                    GiveItemDirectly(0, 30250000, 1)
            else:
                """State 379"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 380"""
                    # weapon:35250000:VP-60LCS
                    GiveItemDirectly(0, 35250000, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 381"""
                    # weapon:30250100:VE-60LCB
                    GiveItemDirectly(0, 30250100, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 382"""
                    # weapon:35250100:VE-60LCB
                    GiveItemDirectly(0, 35250100, 1)
                else:
                    """State 383"""
                    # weapon:30220000:VE-60LCA
                    GiveItemDirectly(0, 30220000, 1)
        elif CompareRNGValue(0, 2) == 1:
            """State 384"""
            SetRNGSeed()
            ShuffleRNGSeed(4)
            if CompareRNGValue(0, 0) == 1:
                """State 385"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 386"""
                    # weapon:35220000:VE-60LCA
                    GiveItemDirectly(0, 35220000, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 387"""
                    # weapon:30240000:KRANICH/60Z
                    GiveItemDirectly(0, 30240000, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 388"""
                    # weapon:35240000:KRANICH/60Z
                    GiveItemDirectly(0, 35240000, 1)
                else:
                    """State 389"""
                    # weapon:30260000:VP-60LCD
                    GiveItemDirectly(0, 30260000, 1)
            elif CompareRNGValue(0, 1) == 1:
                """State 390"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 391"""
                    # weapon:35260000:VP-60LCD
                    GiveItemDirectly(0, 35260000, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 392"""
                    # weapon:30400000:DF-GA-09 SHAO-WEI
                    GiveItemDirectly(0, 30400000, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 393"""
                    # weapon:35400000:DF-GA-09 SHAO-WEI
                    GiveItemDirectly(0, 35400000, 1)
                else:
                    """State 394"""
                    # weapon:30300000:BO-044 HUXLEY
                    GiveItemDirectly(0, 30300000, 1)
            elif CompareRNGValue(0, 2) == 1:
                """State 395"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 396"""
                    # weapon:35300000:BO-044 HUXLEY
                    GiveItemDirectly(0, 35300000, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 397"""
                    # weapon:30300100:45-091 ORBT
                    GiveItemDirectly(0, 30300100, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 398"""
                    # weapon:35300100:45-091 ORBT
                    GiveItemDirectly(0, 35300100, 1)
                else:
                    """State 399"""
                    # weapon:30140100:Vvc-700LD
                    GiveItemDirectly(0, 30140100, 1)
            else:
                """State 400"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 401"""
                    # weapon:35140100:Vvc-700LD
                    GiveItemDirectly(0, 35140100, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 402"""
                    # weapon:30150100:VP-60LT
                    GiveItemDirectly(0, 30150100, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 403"""
                    # weapon:35150100:VP-60LT
                    GiveItemDirectly(0, 35150100, 1)
                else:
                    """State 404"""
                    # weapon:30310000:EULE/60D
                    GiveItemDirectly(0, 30310000, 1)
        else:
            """State 405"""
            SetRNGSeed()
            ShuffleRNGSeed(3)
            if CompareRNGValue(0, 0) == 1:
                """State 406"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 407"""
                    # weapon:35310000:EULE/60D
                    GiveItemDirectly(0, 35310000, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 408"""
                    # weapon:30270000:VE-60SNA
                    GiveItemDirectly(0, 30270000, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 409"""
                    # weapon:35270000:VE-60SNA
                    GiveItemDirectly(0, 35270000, 1)
                else:
                    """State 410"""
                    # weapon:25000000:VP-61PB
                    GiveItemDirectly(0, 25000000, 1)
            elif CompareRNGValue(0, 1) == 1:
                """State 411"""
                SetRNGSeed()
                ShuffleRNGSeed(4)
                if CompareRNGValue(0, 0) == 1:
                    """State 412"""
                    # weapon:25000100:SI-24: SU-Q5
                    GiveItemDirectly(0, 25000100, 1)
                elif CompareRNGValue(0, 1) == 1:
                    """State 413"""
                    # weapon:25010000:VP-61PS
                    GiveItemDirectly(0, 25010000, 1)
                elif CompareRNGValue(0, 2) == 1:
                    """State 414"""
                    # weapon:25010100:SI-27: SU-R8
                    GiveItemDirectly(0, 25010100, 1)
                else:
                    """State 415"""
                    # weapon:25010200:SI-29: SU-TT/C
                    GiveItemDirectly(0, 25010200, 1)
            else:
                """State 416"""
                SetRNGSeed()
                ShuffleRNGSeed(2)
                if CompareRNGValue(0, 0) == 1:
                    """State 417"""
                    # weapon:25010300:IB-C03W4: NGI 028
                    GiveItemDirectly(0, 25010300, 1)
                else:
                    """State 418"""
                    # weapon:25020000:VE-61PSA
                    GiveItemDirectly(0, 25020000, 1)
    """State 427"""
    SetEventFlag(flag1, 1)
    return 0

def t001000000_4():
    """State 0"""
    SetEventFlag(9901, 0)
    SetEventFlag(9902, 0)
    SetEventFlag(9903, 0)
    SetEventFlag(9904, 0)
    SetEventFlag(9905, 0)
    SetEventFlag(9906, 0)
    SetEventFlag(9907, 0)
    SetEventFlag(9908, 0)
    SetEventFlag(9909, 0)
    SetEventFlag(9910, 0)
    SetEventFlag(9911, 0)
    SetEventFlag(9912, 0)
    SetEventFlag(9913, 0)
    SetEventFlag(9914, 0)
    SetEventFlag(9915, 0)
    SetEventFlag(9916, 0)
    SetEventFlag(9917, 0)
    SetEventFlag(9918, 0)
    SetEventFlag(9919, 0)
    SetEventFlag(9920, 0)
    SetEventFlag(9921, 0)
    SetEventFlag(9922, 0)
    SetEventFlag(9923, 0)
    SetEventFlag(9924, 0)
    SetEventFlag(9925, 0)
    SetEventFlag(9926, 0)
    SetEventFlag(9927, 0)
    SetEventFlag(9928, 0)
    SetEventFlag(9929, 0)
    SetEventFlag(9930, 0)
    SetEventFlag(9931, 0)
    SetEventFlag(9932, 0)
    SetEventFlag(9933, 0)
    SetEventFlag(9934, 0)
    SetEventFlag(9935, 0)
    SetEventFlag(9936, 0)
    SetEventFlag(9937, 0)
    SetEventFlag(9938, 0)
    SetEventFlag(9939, 0)
    SetEventFlag(9940, 0)
    SetEventFlag(9941, 0)
    SetEventFlag(9942, 0)
    SetEventFlag(9943, 0)
    SetEventFlag(9944, 0)
    SetEventFlag(9945, 0)
    SetEventFlag(9946, 0)
    SetEventFlag(9947, 0)
    SetEventFlag(9948, 0)
    SetEventFlag(9949, 0)
    SetEventFlag(9950, 0)
    SetEventFlag(9951, 0)
    SetEventFlag(9952, 0)
    # mission:7970:"Destroy Artillery Installations"
    SetMissionState(7970, 0, 0)
    # mission:7970:"Destroy Artillery Installations"
    SetMissionState(7970, 1, 0)
    # mission:7920:"Grid 135 Cleanup"
    SetMissionState(7920, 0, 0)
    # mission:7920:"Grid 135 Cleanup"
    SetMissionState(7920, 1, 0)
    # eventflag:3122:	Mission_Unlocking 	Mission_解禁用
    SetEventFlag(3122, 0)
    # mission:7900:"Destroy the Transport Helicopters"
    SetMissionState(7900, 0, 0)
    # mission:7900:"Destroy the Transport Helicopters"
    SetMissionState(7900, 1, 0)
    # mission:7980:"Destroy the Tester AC"
    SetMissionState(7980, 0, 0)
    # mission:7980:"Destroy the Tester AC"
    SetMissionState(7980, 1, 0)
    # mission:2020:"Attack the Dam Complex"
    SetMissionState(2020, 0, 0)
    # mission:2020:"Attack the Dam Complex"
    SetMissionState(2020, 1, 0)
    # mission:2025:"Attack the Dam Complex"
    SetMissionState(2025, 0, 0)
    # mission:2025:"Attack the Dam Complex"
    SetMissionState(2025, 1, 0)
    # mission:2080:"Destroy the Weaponized Mining Ship"
    SetMissionState(2080, 0, 0)
    # mission:2080:"Destroy the Weaponized Mining Ship"
    SetMissionState(2080, 1, 0)
    # mission:2030:"Operation Wallclimber"
    SetMissionState(2030, 0, 0)
    # mission:2030:"Operation Wallclimber"
    SetMissionState(2030, 1, 0)
    # mission:2100:"Retrieve Combat Logs"
    SetMissionState(2100, 0, 0)
    # mission:2100:"Retrieve Combat Logs"
    SetMissionState(2100, 1, 0)
    # mission:2060:"Investigate BAWS Arsenal No. 2"
    SetMissionState(2060, 0, 0)
    # mission:2060:"Investigate BAWS Arsenal No. 2"
    SetMissionState(2060, 1, 0)
    # mission:2050:"Attack the Watchpoint"
    SetMissionState(2050, 0, 0)
    # mission:2050:"Attack the Watchpoint"
    SetMissionState(2050, 1, 0)
    # mission:2120:"Infiltrate Grid 086"
    SetMissionState(2120, 0, 0)
    # mission:2120:"Infiltrate Grid 086"
    SetMissionState(2120, 1, 0)
    # mission:7960:"Eliminate the Doser Faction"
    SetMissionState(7960, 0, 0)
    # mission:7960:"Eliminate the Doser Faction"
    SetMissionState(7960, 1, 0)
    # mission:2180:"Ocean Crossing"
    SetMissionState(2180, 0, 0)
    # mission:2180:"Ocean Crossing"
    SetMissionState(2180, 1, 0)
    # mission:3011:"Steal the Survey Data"
    SetMissionState(3011, 0, 0)
    # mission:3011:"Steal the Survey Data"
    SetMissionState(3011, 1, 0)
    # mission:3030:"Attack the Refueling Base"
    SetMissionState(3030, 0, 0)
    # mission:3030:"Attack the Refueling Base"
    SetMissionState(3030, 1, 0)
    # mission:2170:"Eliminate V.VII"
    SetMissionState(2170, 0, 0)
    # mission:2170:"Eliminate V.VII"
    SetMissionState(2170, 1, 0)
    # mission:3420:"Tunnel Sabotage"
    SetMissionState(3420, 0, 0)
    # mission:3420:"Tunnel Sabotage"
    SetMissionState(3420, 1, 0)
    # mission:5100:"Survey the Uninhabited Floating City"
    SetMissionState(5100, 0, 0)
    # mission:5100:"Survey the Uninhabited Floating City"
    SetMissionState(5100, 1, 0)
    # mission:2220:"Heavy Missile Launch Support"
    SetMissionState(2220, 0, 0)
    # mission:2220:"Heavy Missile Launch Support"
    SetMissionState(2220, 1, 0)
    # mission:7990:"Eliminate the Enforcement Squads"
    SetMissionState(7990, 0, 0)
    # mission:7990:"Eliminate the Enforcement Squads"
    SetMissionState(7990, 1, 0)
    # mission:3430:"Destroy the Special Forces Craft"
    SetMissionState(3430, 0, 0)
    # mission:3430:"Destroy the Special Forces Craft"
    SetMissionState(3430, 1, 0)
    # mission:3043:"Attack the Old Spaceport"
    SetMissionState(3043, 0, 0)
    # mission:3043:"Attack the Old Spaceport"
    SetMissionState(3043, 1, 0)
    # mission:3320:"Eliminate "Honest" Brute"
    SetMissionState(3320, 0, 0)
    # mission:3320:"Eliminate "Honest" Brute"
    SetMissionState(3320, 1, 0)
    # mission:7950:"Defend the Old Spaceport"
    SetMissionState(7950, 0, 0)
    # mission:7950:"Defend the Old Spaceport"
    SetMissionState(7950, 1, 0)
    # mission:3500:"Historic Data Recovery"
    SetMissionState(3500, 0, 0)
    # mission:3500:"Historic Data Recovery"
    SetMissionState(3500, 1, 0)
    # mission:3230:"Destroy the Ice Worm"
    SetMissionState(3230, 0, 0)
    # mission:3230:"Destroy the Ice Worm"
    SetMissionState(3230, 1, 0)
    # mission:4000:"Underground Exploration – Depth 1"
    SetMissionState(4000, 0, 0)
    # mission:4000:"Underground Exploration – Depth 1"
    SetMissionState(4000, 1, 0)
    # mission:4010:"Underground Exploration – Depth 2"
    SetMissionState(4010, 0, 0)
    # mission:4010:"Underground Exploration – Depth 2"
    SetMissionState(4010, 1, 0)
    # mission:4020:"Underground Exploration – Depth 3"
    SetMissionState(4020, 0, 0)
    # mission:4020:"Underground Exploration – Depth 3"
    SetMissionState(4020, 1, 0)
    # mission:7930:"Intercept the Redguns"
    SetMissionState(7930, 0, 0)
    # mission:7930:"Intercept the Redguns"
    SetMissionState(7930, 1, 0)
    # mission:4110:"Ambush the Vespers"
    SetMissionState(4110, 0, 0)
    # mission:4110:"Ambush the Vespers"
    SetMissionState(4110, 1, 0)
    # mission:4021:"Unknown Territory Survey"
    SetMissionState(4021, 0, 0)
    # mission:4021:"Unknown Territory Survey"
    SetMissionState(4021, 1, 0)
    # mission:4030:"Reach the Coral Convergence"
    SetMissionState(4030, 0, 0)
    # mission:4030:"Reach the Coral Convergence"
    SetMissionState(4030, 1, 0)
    # mission:4200:"Escape"
    SetMissionState(4200, 0, 0)
    # mission:4200:"Escape"
    SetMissionState(4200, 1, 0)
    # mission:5010:"Take the Uninhabited Floating City"
    SetMissionState(5010, 0, 0)
    # mission:5010:"Take the Uninhabited Floating City"
    SetMissionState(5010, 1, 0)
    # mission:5020:"Intercept the Corporate Forces"
    SetMissionState(5020, 0, 0)
    # mission:5020:"Intercept the Corporate Forces"
    SetMissionState(5020, 1, 0)
    # mission:5050:"Eliminate "Cinder" Carla"
    SetMissionState(5050, 0, 0)
    # mission:5050:"Eliminate "Cinder" Carla"
    SetMissionState(5050, 1, 0)
    # mission:5040:"Breach the Kármán Line"
    SetMissionState(5040, 0, 0)
    # mission:5040:"Breach the Kármán Line"
    SetMissionState(5040, 1, 0)
    # mission:5030:"Destroy the Drive Block"
    SetMissionState(5030, 0, 0)
    # mission:5030:"Destroy the Drive Block"
    SetMissionState(5030, 1, 0)
    # mission:6000:"Shut Down the Closure Satellites"
    SetMissionState(6000, 0, 0)
    # mission:6000:"Shut Down the Closure Satellites"
    SetMissionState(6000, 1, 0)
    # mission:6010:"Bring Down the Xylem"
    SetMissionState(6010, 0, 0)
    # mission:6010:"Bring Down the Xylem"
    SetMissionState(6010, 1, 0)
    # mission:2025:"Attack the Dam Complex"
    SetMissionState(2025, 0, 0)
    # mission:2025:"Attack the Dam Complex"
    SetMissionState(2025, 1, 0)
    # mission:7910:"Prevent Corporate Salvage of New Tech"
    SetMissionState(7910, 0, 0)
    # mission:7910:"Prevent Corporate Salvage of New Tech"
    SetMissionState(7910, 1, 0)
    # mission:2240:"Defend the Dam Complex"
    SetMissionState(2240, 0, 0)
    # mission:2240:"Defend the Dam Complex"
    SetMissionState(2240, 1, 0)
    # mission:2250:"Escort the Weaponized Mining Ship"
    SetMissionState(2250, 0, 0)
    # mission:2250:"Escort the Weaponized Mining Ship"
    SetMissionState(2250, 1, 0)
    # mission:2140:"Prisoner Rescue"
    SetMissionState(2140, 0, 0)
    # mission:2140:"Prisoner Rescue"
    SetMissionState(2140, 1, 0)
    # mission:2200:"Obstruct the Mandatory Inspection"
    SetMissionState(2200, 0, 0)
    # mission:2200:"Obstruct the Mandatory Inspection"
    SetMissionState(2200, 1, 0)
    # mission:2230:"Stop the Secret Data Breach"
    SetMissionState(2230, 0, 0)
    # mission:2230:"Stop the Secret Data Breach"
    SetMissionState(2230, 1, 0)
    # mission:2211:"Coral Export Denial"
    SetMissionState(2211, 0, 0)
    # mission:2211:"Coral Export Denial"
    SetMissionState(2211, 1, 0)
    # mission:4100:"MIA"
    SetMissionState(4100, 0, 0)
    # mission:4100:"MIA"
    SetMissionState(4100, 1, 0)
    # mission:5110:"Regain Control of the Xylem"
    SetMissionState(5110, 0, 0)
    # mission:5110:"Regain Control of the Xylem"
    SetMissionState(5110, 1, 0)
    # mission:6020:"Coral Release"
    SetMissionState(6020, 0, 0)
    # mission:6020:"Coral Release"
    SetMissionState(6020, 1, 0)
    return 1

def t001000000_1000():
    """State 0,13"""
    SetEventFlag(9900, 1)
    assert t001000000_x49()
    """State 7"""
    # eventflag:3135:	mission grayed out 	ミッショングレーアウト
    SetEventFlag(3135, 1)
    c1_117(0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1, 0)
    # eventflag:3409:	[Garage] Judgment by watching the story production_Chapter 1 Entered the garage for the first time 	【ガレージ】ストーリー演出を見た判定_チャプター1初めてガレージに入った
    if GetCurrentStateElapsedTime() > 1.5 and not GetEventFlag(3409):
        """State 4"""
        # eventflag:3220:	BGM reset judgment at garage IN 	ガレージIN時のBGMリセット判定
        SetEventFlag(3220, 1)
        # eventflag:3210:	Silent start determination 	無音スタート判定
        SetEventFlag(3210, 1)
        # eventflag:3200:	Menu non-display judgment 	メニュー非表示判定
        SetEventFlag(3200, 1)
        # eventflag:3123:	Assemble_Unlocking 	Assemble_解禁用
        SetEventFlag(3123, 1)
        # eventflag:3125:	Design_Unlocking 	Design_解禁用
        SetEventFlag(3125, 1)
        c1_229(0)
        assert GetCurrentStateElapsedFrames() > 1
        """State 5"""
        GiveSpEffectToPlayer(5020)
        if UnkGameCycle() > 1:
            """State 8"""
            # eventflag:3126:	AC_Test_Unban 	AC_Test_解禁用
            SetEventFlag(3126, 1)
            # eventflag:3124:	Paint_Unlocking 	Paint_解禁用
            SetEventFlag(3124, 1)
            # eventflag:3409:	[Garage] Judgment by watching the story production_Chapter 1 Entered the garage for the first time 	【ガレージ】ストーリー演出を見た判定_チャプター1初めてガレージに入った
            SetEventFlag(3409, 1)
            # eventflag:3127:	Market_Unlocking 	Market_解禁用
            SetEventFlag(3127, 1)
            # eventflag:3130:	AC_Arena_Unban 	AC_Arena_解禁用
            SetEventFlag(3130, 1)
            # eventflag:3131:	OS_Update_Unban 	OS_Update_解禁用
            SetEventFlag(3131, 1)
            # eventflag:3133:	ONLINE_Arena_Unlocking 	ONLINE_Arena_解禁用
            SetEventFlag(3133, 1)
            # eventflag:3134:	replaymission for unlocking 	replaymission 解禁用
            SetEventFlag(3134, 1)
            # eventflag:3150:	Arena unlock progress 1 	アリーナ解禁進行度1
            SetEventFlag(3150, 1)
            # eventflag:3151:	Arena unlock progress 2 	アリーナ解禁進行度2
            SetEventFlag(3151, 1)
            # eventflag:3152:	Arena unlock progress 3 	アリーナ解禁進行度3
            SetEventFlag(3152, 1)
            # eventflag:3153:	Arena unlock progress 4 	アリーナ解禁進行度4
            SetEventFlag(3153, 1)
            # eventflag:3154:	Arena unlock progress 5 	アリーナ解禁進行度5
            SetEventFlag(3154, 1)
            # eventflag:3155:	Arena unlock progress 6 	アリーナ解禁進行度6
            SetEventFlag(3155, 1)
            # eventflag:3136:	reserve 11 	予備11
            SetEventFlag(3136, 1)
            if UnkGameCycle() > 2:
                """State 10"""
                # eventflag:3156:	Arena unlock progress 7 	アリーナ解禁進行度7
                SetEventFlag(3156, 1)
                # eventflag:3157:	Arena unlock progress 8 	アリーナ解禁進行度8
                SetEventFlag(3157, 1)
                # eventflag:3158:	Arena unlock progress 9 	アリーナ解禁進行度9
                SetEventFlag(3158, 1)
            else:
                pass
            """State 9"""
            # mission:9202:"Intermediate Support 1: Assembling an AC"
            SetMissionState(9202, 0, 1)
            # mission:9200:"Beginner Training 1: Basic Controls"
            SetMissionState(9200, 0, 1)
            # mission:9201:"Beginner Training 2: Combat Fundamentals"
            SetMissionState(9201, 0, 1)
            # mission:9203:"Intermediate Support 2: Reverse-Jointed ACs"
            SetMissionState(9203, 0, 1)
            # mission:9204:"Intermediate Support 3: Tetrapod ACs"
            SetMissionState(9204, 0, 1)
            # mission:9205:"Intermediate Support 4: Tank ACs"
            SetMissionState(9205, 0, 1)
            # eventflag:6438:	Tremo 7 released 	トレモ７出した
            if GetEventFlag(6438) == 1:
                """State 11"""
                # mission:9206:"Advanced Mercenary Certification"
                SetMissionState(9206, 0, 1)
            else:
                pass
        else:
            """State 6"""
            # eventflag:3126:	AC_Test_Unban 	AC_Test_解禁用
            SetEventFlag(3126, 1)
            # eventflag:3124:	Paint_Unlocking 	Paint_解禁用
            SetEventFlag(3124, 1)
            # eventflag:3409:	[Garage] Judgment by watching the story production_Chapter 1 Entered the garage for the first time 	【ガレージ】ストーリー演出を見た判定_チャプター1初めてガレージに入った
            SetEventFlag(3409, 1)
            # eventflag:3135:	mission grayed out 	ミッショングレーアウト
            SetEventFlag(3135, 1)
            # eventflag:3134:	replaymission for unlocking 	replaymission 解禁用
            SetEventFlag(3134, 1)
    elif GetCurrentStateElapsedTime() > 1.5:
        """State 2"""
        StartEvent(0, 2572)
        # eventflag:3220:	BGM reset judgment at garage IN 	ガレージIN時のBGMリセット判定
        SetEventFlag(3220, 1)
        # eventflag:3200:	Menu non-display judgment 	メニュー非表示判定
        SetEventFlag(3200, 1)
        assert GetCurrentStateElapsedFrames() > 1
        """State 3"""
        GiveSpEffectToPlayer(5020)
    """State 12"""
    assert t001000000_x1()
    """State 1"""
    # eventflag:3200:	Menu non-display judgment 	メニュー非表示判定
    SetEventFlag(3200, 0)
    # eventflag:3210:	Silent start determination 	無音スタート判定
    SetEventFlag(3210, 0)
    c1_228()
    assert t001000000_2()
    """State 14"""
    return 1

def t001000000_x0():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t001000000_x1():
    """State 0,1"""
    c1_230(1)
    # eventflag:3139:	reserve 14 	予備14
    SetEventFlag(3139, 1)
    if not GetChapter():
        """State 20"""
        call = t001000000_x38()
        # eventflag:3920:	whispered flag 	ひそひそ話をしたフラグ
        if call.Done() and GetEventFlag(3920) == 1:
            """State 2"""
            # eventflag:3920:	whispered flag 	ひそひそ話をしたフラグ
            SetEventFlag(3920, 0)
        elif call.Done():
            """State 3"""
            c1_117(0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0.5, 0)
            assert f336() == 1
        """State 13"""
        assert t001000000_x7()
    elif GetChapter() == 1:
        """State 21"""
        call = t001000000_x39()
        # eventflag:3920:	whispered flag 	ひそひそ話をしたフラグ
        if call.Done() and GetEventFlag(3920) == 1:
            """State 4"""
            # eventflag:3920:	whispered flag 	ひそひそ話をしたフラグ
            SetEventFlag(3920, 0)
        elif call.Done():
            """State 5"""
            c1_117(0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0.5, 0)
            assert f336() == 1
        """State 14"""
        assert t001000000_x9()
    elif GetChapter() == 2:
        """State 22"""
        call = t001000000_x40()
        # eventflag:3920:	whispered flag 	ひそひそ話をしたフラグ
        if call.Done() and GetEventFlag(3920) == 1:
            """State 7"""
            # eventflag:3920:	whispered flag 	ひそひそ話をしたフラグ
            SetEventFlag(3920, 0)
        elif call.Done():
            """State 6"""
            c1_117(0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0.5, 0)
            assert f336() == 1
        """State 15"""
        assert t001000000_x11()
    elif GetChapter() == 3:
        """State 23"""
        call = t001000000_x41()
        # eventflag:3920:	whispered flag 	ひそひそ話をしたフラグ
        if call.Done() and GetEventFlag(3920) == 1:
            """State 9"""
            # eventflag:3920:	whispered flag 	ひそひそ話をしたフラグ
            SetEventFlag(3920, 0)
        elif call.Done():
            """State 8"""
            c1_117(0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0.5, 0)
            assert f336() == 1
        """State 16"""
        assert t001000000_x12()
    elif GetChapter() == 4:
        """State 10"""
        if True:
            """State 11"""
            c1_117(0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0.5, 0)
            assert f336() == 1
        else:
            """State 12"""
            # eventflag:3920:	whispered flag 	ひそひそ話をしたフラグ
            SetEventFlag(3920, 0)
        """State 17"""
        assert t001000000_x13()
    """State 18"""
    assert t001000000_x27()
    """State 19"""
    assert t001000000_x31()
    """State 24"""
    c1_230(0)
    # eventflag:3139:	reserve 14 	予備14
    SetEventFlag(3139, 0)
    return 0

def t001000000_x2():
    """State 0"""
    # mission:7970:"Destroy Artillery Installations"
    if not UnkMissionComplete(7970, 1) == 1 and not UnkMissionComplete(7970, 0) == 1:
        """State 39"""
        # mission:7970:"Destroy Artillery Installations"
        SetMissionState(7970, 0, 1)
        # mission:7920:"Grid 135 Cleanup"
        SetMissionState(7920, 0, 1)
        # eventflag:3122:	Mission_Unlocking 	Mission_解禁用
        SetEventFlag(3122, 1)
    else:
        pass
    """State 38"""
    # mission:7970:"Destroy Artillery Installations", mission:7920:"Grid 135 Cleanup"
    if UnkMissionComplete(7970, 1) == 1 and UnkMissionComplete(7920, 1) == 1:
        """State 1,41"""
        # mission:7900:"Destroy the Transport Helicopters"
        if not UnkMissionComplete(7900, 1) == 1 and not UnkMissionComplete(7900, 0) == 1:
            """State 40"""
            # mission:7900:"Destroy the Transport Helicopters"
            SetMissionState(7900, 0, 1)
            # mission:7980:"Destroy the Tester AC"
            SetMissionState(7980, 0, 1)
        else:
            pass
        """State 42"""
        # mission:7900:"Destroy the Transport Helicopters", mission:7980:"Destroy the Tester AC"
        if UnkMissionComplete(7900, 1) == 1 and UnkMissionComplete(7980, 1) == 1:
            """State 43"""
            # eventflag:2040:	Event flag for PlayGo 	PlayGo用イベントフラグ
            if GetEventFlag(2040) == 1:
                """State 44"""
                # eventflag:3135:	mission grayed out 	ミッショングレーアウト
                SetEventFlag(3135, 1)
            # eventflag:2040:	Event flag for PlayGo 	PlayGo用イベントフラグ
            elif not GetEventFlag(2040):
                """State 45"""
                # eventflag:3135:	mission grayed out 	ミッショングレーアウト
                SetEventFlag(3135, 0)
            """State 3"""
            # eventflag:6000:	A route clear 	Aルートクリア, eventflag:6001:	B route clear 	Bルートクリア
            if GetEventFlag(6000) == 1 and GetEventFlag(6001) == 1:
                """State 31"""
                # mission:2025:"Attack the Dam Complex"
                if not UnkMissionComplete(2025, 0) == 1 and not UnkMissionComplete(2025, 1) == 1:
                    """State 14"""
                    # mission:2025:"Attack the Dam Complex"
                    SetMissionState(2025, 0, 1)
                    # mission:2080:"Destroy the Weaponized Mining Ship"
                    SetMissionState(2080, 0, 1)
                    # mission:2250:"Escort the Weaponized Mining Ship"
                    SetMissionState(2250, 0, 1)
                else:
                    pass
            elif UnkGameCycle() > 1:
                """State 30"""
                # mission:2025:"Attack the Dam Complex"
                if not UnkMissionComplete(2025, 0) == 1 and not UnkMissionComplete(2025, 1) == 1:
                    """State 13"""
                    # mission:2025:"Attack the Dam Complex"
                    SetMissionState(2025, 0, 1)
                    # mission:2080:"Destroy the Weaponized Mining Ship"
                    SetMissionState(2080, 0, 1)
                else:
                    pass
            else:
                """State 29"""
                # mission:2020:"Attack the Dam Complex"
                if not UnkMissionComplete(2020, 0) == 1 and not UnkMissionComplete(2020, 1) == 1:
                    """State 2"""
                    # mission:2020:"Attack the Dam Complex"
                    SetMissionState(2020, 0, 1)
                    # mission:2080:"Destroy the Weaponized Mining Ship"
                    SetMissionState(2080, 0, 1)
                else:
                    pass
            """State 46,4"""
            if UnkGameCycle() > 2:
                """State 16"""
                # mission:2080:"Destroy the Weaponized Mining Ship", mission:2025:"Attack the Dam Complex"
                if UnkMissionComplete(2080, 1) == 1 and UnkMissionComplete(2025, 1) == 1:
                    """State 17,19"""
                    Label('L0')
                    # mission:2030:"Operation Wallclimber"
                    if not UnkMissionComplete(2030, 0) == 1 and not UnkMissionComplete(2030, 1) == 1:
                        """State 6"""
                        # mission:2030:"Operation Wallclimber"
                        SetMissionState(2030, 0, 1)
                    else:
                        pass
                    """State 7"""
                    # mission:2030:"Operation Wallclimber"
                    if UnkMissionComplete(2030, 1) == 1:
                        """State 8"""
                        # eventflag:8101:	8101_In-mission branching event flag_dam destruction_betrayal route_ 	8101_ミッション内分岐用イベントフラグ_ダム破壊_裏切りルート_
                        if GetEventFlag(8101) == 1:
                            """State 21"""
                            # mission:2140:"Prisoner Rescue"
                            if not UnkMissionComplete(2140, 0) == 1 and not UnkMissionComplete(2140, 1) == 1:
                                """State 23"""
                                # mission:2140:"Prisoner Rescue"
                                SetMissionState(2140, 0, 1)
                            else:
                                pass
                        else:
                            """State 20"""
                            # mission:2100:"Retrieve Combat Logs"
                            if not UnkMissionComplete(2100, 0) == 1 and not UnkMissionComplete(2100, 1) == 1:
                                """State 22"""
                                # mission:2100:"Retrieve Combat Logs"
                                SetMissionState(2100, 0, 1)
                            else:
                                pass
                        """State 24"""
                        # mission:2250:"Escort the Weaponized Mining Ship"
                        if UnkMissionComplete(2250, 1) == 1:
                            """State 26"""
                            # mission:2200:"Obstruct the Mandatory Inspection"
                            if not UnkMissionComplete(2200, 0) == 1 and not UnkMissionComplete(2200, 1) == 1:
                                """State 28"""
                                # mission:2200:"Obstruct the Mandatory Inspection"
                                SetMissionState(2200, 0, 1)
                            else:
                                pass
                        # mission:2080:"Destroy the Weaponized Mining Ship"
                        elif UnkMissionComplete(2080, 1) == 1:
                            """State 25"""
                            # mission:2060:"Investigate BAWS Arsenal No. 2"
                            if not UnkMissionComplete(2060, 0) == 1 and not UnkMissionComplete(2060, 1) == 1:
                                """State 27"""
                                # mission:2060:"Investigate BAWS Arsenal No. 2"
                                SetMissionState(2060, 0, 1)
                            else:
                                pass
                        """State 9"""
                        # mission:2100:"Retrieve Combat Logs"
                        if UnkMissionComplete(2100, 1) == 1:
                            """State 32"""
                            Label('L1')
                            if True:
                                """State 33"""
                                # mission:2060:"Investigate BAWS Arsenal No. 2"
                                if UnkMissionComplete(2060, 1) == 1:
                                    """State 35"""
                                    Label('L2')
                                    # mission:2250:"Escort the Weaponized Mining Ship"
                                    if UnkGameCycle() > 2 and UnkMissionComplete(2250, 1) == 1:
                                        """State 37"""
                                        # mission:2055:"Attack the Watchpoint"
                                        if (not UnkMissionComplete(2055, 0) == 1 and not UnkMissionComplete(2055,
                                            1) == 1):
                                            """State 36"""
                                            # mission:2055:"Attack the Watchpoint"
                                            SetMissionState(2055, 0, 1)
                                        else:
                                            pass
                                    else:
                                        """State 34"""
                                        # mission:2050:"Attack the Watchpoint"
                                        if (not UnkMissionComplete(2050, 0) == 1 and not UnkMissionComplete(2050,
                                            1) == 1):
                                            """State 10"""
                                            # mission:2050:"Attack the Watchpoint"
                                            SetMissionState(2050, 0, 1)
                                        else:
                                            pass
                                    """State 11"""
                                    # mission:2050:"Attack the Watchpoint"
                                    if UnkMissionComplete(2050, 1) == 1:
                                        """State 12"""
                                        Label('L3')
                                    # mission:2055:"Attack the Watchpoint"
                                    elif UnkMissionComplete(2055, 1) == 1:
                                        Goto('L3')
                                    else:
                                        pass
                                # mission:2200:"Obstruct the Mandatory Inspection"
                                elif UnkMissionComplete(2200, 1) == 1:
                                    Goto('L2')
                                else:
                                    pass
                            else:
                                pass
                        # mission:2140:"Prisoner Rescue"
                        elif UnkMissionComplete(2140, 1) == 1:
                            Goto('L1')
                        else:
                            pass
                    else:
                        pass
                # mission:2250:"Escort the Weaponized Mining Ship", mission:2025:"Attack the Dam Complex"
                elif UnkMissionComplete(2250, 1) == 1 and UnkMissionComplete(2025, 1) == 1:
                    """State 18"""
                    Goto('L0')
                else:
                    """State 48"""
                    return 1
            # mission:2080:"Destroy the Weaponized Mining Ship", mission:2025:"Attack the Dam Complex"
            elif UnkGameCycle() > 1 and UnkMissionComplete(2080, 1) == 1 and UnkMissionComplete(2025, 1) == 1:
                """State 15"""
                Goto('L0')
            # mission:2080:"Destroy the Weaponized Mining Ship", mission:2020:"Attack the Dam Complex"
            elif UnkMissionComplete(2080, 1) == 1 and UnkMissionComplete(2020, 1) == 1:
                """State 5"""
                Goto('L0')
            else:
                pass
        else:
            pass
    else:
        pass
    """State 47"""
    return 0

def t001000000_x3():
    """State 0"""
    # mission:2120:"Infiltrate Grid 086"
    if not UnkMissionComplete(2120, 0) == 1 and not UnkMissionComplete(2120, 1) == 1:
        """State 1"""
        # mission:2120:"Infiltrate Grid 086"
        SetMissionState(2120, 0, 1)
    else:
        pass
    """State 3"""
    # mission:2120:"Infiltrate Grid 086"
    if UnkMissionComplete(2120, 1) == 1:
        """State 2"""
        # mission:2250:"Escort the Weaponized Mining Ship"
        if UnkMissionComplete(2250, 1) == 1:
            """State 9"""
            Label('L0')
            # mission:2230:"Stop the Secret Data Breach"
            if not UnkMissionComplete(2230, 0) == 1 and not UnkMissionComplete(2230, 1) == 1:
                """State 4"""
                # mission:2230:"Stop the Secret Data Breach"
                SetMissionState(2230, 0, 1)
            else:
                pass
        # eventflag:8101:	8101_In-mission branching event flag_dam destruction_betrayal route_ 	8101_ミッション内分岐用イベントフラグ_ダム破壊_裏切りルート_
        elif GetEventFlag(8101) == 1:
            Goto('L0')
        else:
            """State 8"""
            # mission:7960:"Eliminate the Doser Faction"
            if not UnkMissionComplete(7960, 0) == 1 and not UnkMissionComplete(7960, 1) == 1:
                """State 10"""
                # mission:7960:"Eliminate the Doser Faction"
                SetMissionState(7960, 0, 1)
            else:
                pass
        """State 5"""
        # mission:2230:"Stop the Secret Data Breach"
        if UnkMissionComplete(2230, 1) == 1:
            """State 7"""
            Label('L1')
            # mission:2180:"Ocean Crossing"
            if not UnkMissionComplete(2180, 0) == 1 and not UnkMissionComplete(2180, 1) == 1:
                """State 6"""
                # mission:2180:"Ocean Crossing"
                SetMissionState(2180, 0, 1)
            else:
                pass
        # mission:7960:"Eliminate the Doser Faction"
        elif UnkMissionComplete(7960, 1) == 1:
            Goto('L1')
        else:
            pass
    else:
        pass
    """State 11"""
    return 0

def t001000000_x4():
    """State 0"""
    # mission:3011:"Steal the Survey Data"
    if not UnkMissionComplete(3011, 0) == 1 and not UnkMissionComplete(3011, 1) == 1:
        """State 1"""
        # mission:3011:"Steal the Survey Data"
        SetMissionState(3011, 0, 1)
    else:
        pass
    """State 3"""
    # mission:3011:"Steal the Survey Data"
    if UnkMissionComplete(3011, 1) == 1:
        """State 2"""
        if UnkGameCycle() > 1:
            """State 12"""
            # mission:3030:"Attack the Refueling Base"
            if not UnkMissionComplete(3030, 0) == 1 and not UnkMissionComplete(3030, 1) == 1:
                """State 10"""
                # mission:3030:"Attack the Refueling Base"
                SetMissionState(3030, 0, 1)
                # mission:3420:"Tunnel Sabotage"
                SetMissionState(3420, 0, 1)
                # mission:2170:"Eliminate V.VII"
                SetMissionState(2170, 0, 1)
                # mission:7910:"Prevent Corporate Salvage of New Tech"
                SetMissionState(7910, 0, 1)
            else:
                pass
        else:
            """State 11"""
            # mission:3030:"Attack the Refueling Base"
            if not UnkMissionComplete(3030, 0) == 1 and not UnkMissionComplete(3030, 1) == 1:
                """State 9"""
                # mission:3030:"Attack the Refueling Base"
                SetMissionState(3030, 0, 1)
                # mission:3420:"Tunnel Sabotage"
                SetMissionState(3420, 0, 1)
                # mission:2170:"Eliminate V.VII"
                SetMissionState(2170, 0, 1)
            else:
                pass
        """State 4"""
        # mission:3030:"Attack the Refueling Base", mission:3420:"Tunnel Sabotage", mission:2170:"Eliminate V.VII"
        if (UnkMissionComplete(3030, 1) == 1 and UnkMissionComplete(3420, 1) == 1 and UnkMissionComplete(2170,
            1) == 1):
            """State 13,5"""
            Label('L0')
            # mission:2250:"Escort the Weaponized Mining Ship"
            if UnkGameCycle() > 2 and UnkMissionComplete(2250, 1) == 1:
                """State 27"""
                # mission:5105:"Survey the Uninhabited Floating City"
                if not UnkMissionComplete(5105, 1) == 1 and not UnkMissionComplete(5105, 0) == 1:
                    """State 15"""
                    # mission:5105:"Survey the Uninhabited Floating City"
                    SetMissionState(5105, 0, 1)
                    """State 29"""
                    Label('L1')
                    # mission:2220:"Heavy Missile Launch Support"
                    SetMissionState(2220, 0, 1)
                    # mission:3430:"Destroy the Special Forces Craft"
                    SetMissionState(3430, 0, 1)
                    # mission:7990:"Eliminate the Enforcement Squads"
                    SetMissionState(7990, 0, 1)
                else:
                    """State 30"""
                    Label('L2')
            # mission:5100:"Survey the Uninhabited Floating City"
            elif not UnkMissionComplete(5100, 0) == 1 and not UnkMissionComplete(5100, 1) == 1:
                """State 16"""
                # mission:5100:"Survey the Uninhabited Floating City"
                SetMissionState(5100, 0, 1)
                if True:
                    Goto('L1')
                else:
                    pass
            else:
                Goto('L2')
            """State 6"""
            # mission:5100:"Survey the Uninhabited Floating City", mission:2220:"Heavy Missile Launch Support", mission:7990:"Eliminate the Enforcement Squads"
            if (UnkMissionComplete(5100, 1) == 1 and UnkMissionComplete(2220, 1) == 1 and UnkMissionComplete(7990,
                1) == 1):
                """State 7"""
                Label('L3')
                # mission:3043:"Attack the Old Spaceport"
                if not UnkMissionComplete(3043, 0) == 1 and not UnkMissionComplete(3043, 1) == 1:
                    """State 8"""
                    # mission:3043:"Attack the Old Spaceport"
                    SetMissionState(3043, 0, 1)
                else:
                    pass
                """State 17"""
                # mission:3043:"Attack the Old Spaceport"
                if UnkMissionComplete(3043, 1) == 1:
                    """State 19"""
                    # mission:3043:"Attack the Old Spaceport"
                    SetMissionState(3043, 0, 1)
                    # mission:7910:"Prevent Corporate Salvage of New Tech"
                    if UnkMissionComplete(7910, 1) == 1:
                        """State 21"""
                        # mission:2250:"Escort the Weaponized Mining Ship"
                        if UnkMissionComplete(2250, 1) == 1:
                            """State 28"""
                            # mission:2211:"Coral Export Denial"
                            if not UnkMissionComplete(2211, 0) == 1 and not UnkMissionComplete(2211, 1) == 1:
                                """State 24"""
                                # mission:3500:"Historic Data Recovery"
                                SetMissionState(3500, 0, 1)
                                # mission:2211:"Coral Export Denial"
                                SetMissionState(2211, 0, 1)
                                # mission:2240:"Defend the Dam Complex"
                                SetMissionState(2240, 0, 1)
                                # mission:3320:"Eliminate "Honest" Brute"
                                SetMissionState(3320, 0, 1)
                            else:
                                pass
                        # mission:3320:"Eliminate "Honest" Brute"
                        elif not UnkMissionComplete(3320, 0) == 1 and not UnkMissionComplete(3320, 1) == 1:
                            """State 23"""
                            # mission:2240:"Defend the Dam Complex"
                            SetMissionState(2240, 0, 1)
                            # mission:3320:"Eliminate "Honest" Brute"
                            SetMissionState(3320, 0, 1)
                            # mission:3500:"Historic Data Recovery"
                            SetMissionState(3500, 0, 1)
                        else:
                            pass
                    else:
                        """State 20"""
                        # mission:2250:"Escort the Weaponized Mining Ship"
                        if UnkMissionComplete(2250, 1) == 1:
                            """State 32"""
                            # mission:2211:"Coral Export Denial"
                            if not UnkMissionComplete(2211, 0) == 1 and not UnkMissionComplete(2211, 1) == 1:
                                """State 31"""
                                # mission:7950:"Defend the Old Spaceport"
                                SetMissionState(7950, 0, 1)
                                # mission:3320:"Eliminate "Honest" Brute"
                                SetMissionState(3320, 0, 1)
                                # mission:3500:"Historic Data Recovery"
                                SetMissionState(3500, 0, 1)
                                # mission:2211:"Coral Export Denial"
                                SetMissionState(2211, 0, 1)
                            else:
                                pass
                        # mission:3320:"Eliminate "Honest" Brute"
                        elif not UnkMissionComplete(3320, 0) == 1 and not UnkMissionComplete(3320, 1) == 1:
                            """State 18"""
                            # mission:7950:"Defend the Old Spaceport"
                            SetMissionState(7950, 0, 1)
                            # mission:3320:"Eliminate "Honest" Brute"
                            SetMissionState(3320, 0, 1)
                            # mission:3500:"Historic Data Recovery"
                            SetMissionState(3500, 0, 1)
                        else:
                            pass
                    """State 22"""
                    # mission:3320:"Eliminate "Honest" Brute", mission:2240:"Defend the Dam Complex", mission:3500:"Historic Data Recovery"
                    if (UnkMissionComplete(3320, 1) == 1 and UnkMissionComplete(2240, 1) == 1 and UnkMissionComplete(3500,
                        1) == 1):
                        """State 25"""
                        Label('L4')
                        # mission:3230:"Destroy the Ice Worm"
                        assert not UnkMissionComplete(3230, 0) == 1 and not UnkMissionComplete(3230, 1) == 1
                        """State 26"""
                        # mission:3230:"Destroy the Ice Worm"
                        SetMissionState(3230, 0, 1)
                    # mission:3320:"Eliminate "Honest" Brute", mission:7950:"Defend the Old Spaceport", mission:3500:"Historic Data Recovery"
                    elif (UnkMissionComplete(3320, 1) == 1 and UnkMissionComplete(7950, 1) == 1 and UnkMissionComplete(3500,
                          1) == 1):
                        Goto('L4')
                    # mission:3320:"Eliminate "Honest" Brute", mission:2240:"Defend the Dam Complex", mission:2211:"Coral Export Denial"
                    elif (UnkMissionComplete(3320, 1) == 1 and UnkMissionComplete(2240, 1) == 1 and UnkMissionComplete(2211,
                          1) == 1):
                        Goto('L4')
                    # mission:3320:"Eliminate "Honest" Brute", mission:7950:"Defend the Old Spaceport", mission:2211:"Coral Export Denial"
                    elif (UnkMissionComplete(3320, 1) == 1 and UnkMissionComplete(7950, 1) == 1 and UnkMissionComplete(2211,
                          1) == 1):
                        Goto('L4')
                    else:
                        pass
                # mission:3230:"Destroy the Ice Worm"
                elif UnkMissionComplete(3230, 1) == 1:
                    pass
            # mission:5105:"Survey the Uninhabited Floating City", mission:2220:"Heavy Missile Launch Support", mission:7990:"Eliminate the Enforcement Squads"
            elif (UnkMissionComplete(5105, 1) == 1 and UnkMissionComplete(2220, 1) == 1 and UnkMissionComplete(7990,
                  1) == 1):
                Goto('L3')
            # mission:5105:"Survey the Uninhabited Floating City", mission:3430:"Destroy the Special Forces Craft", mission:2220:"Heavy Missile Launch Support"
            elif (UnkMissionComplete(5105, 1) == 1 and UnkMissionComplete(3430, 1) == 1 and UnkMissionComplete(2220,
                  1) == 1):
                Goto('L3')
            # mission:2220:"Heavy Missile Launch Support", mission:3430:"Destroy the Special Forces Craft", mission:5100:"Survey the Uninhabited Floating City"
            elif (UnkMissionComplete(2220, 1) == 1 and UnkMissionComplete(3430, 1) == 1 and UnkMissionComplete(5100,
                  1) == 1):
                Goto('L3')
            else:
                pass
        # mission:3030:"Attack the Refueling Base", mission:7910:"Prevent Corporate Salvage of New Tech", mission:2170:"Eliminate V.VII"
        elif (UnkMissionComplete(3030, 1) == 1 and UnkMissionComplete(7910, 1) == 1 and UnkMissionComplete(2170,
              1) == 1):
            """State 14"""
            Goto('L0')
        else:
            pass
    else:
        pass
    """State 33"""
    return 0

def t001000000_x5():
    """State 0"""
    # mission:4000:"Underground Exploration – Depth 1"
    if not UnkMissionComplete(4000, 0) == 1 and not UnkMissionComplete(4000, 1) == 1:
        """State 1"""
        # mission:4000:"Underground Exploration – Depth 1"
        SetMissionState(4000, 0, 1)
    else:
        pass
    """State 3"""
    # mission:4000:"Underground Exploration – Depth 1"
    if UnkMissionComplete(4000, 1) == 1:
        """State 2"""
        # mission:2211:"Coral Export Denial"
        if UnkMissionComplete(2211, 1) == 1:
            """State 25"""
            Label('L0')
            # mission:4015:"Underground Exploration – Depth 2"
            SetMissionState(4015, 0, 1)
            # mission:4015:"Underground Exploration – Depth 2"
            if UnkMissionComplete(4015, 0) == 1 and UnkMissionComplete(4015, 1) == 1:
                """State 13"""
                # mission:4015:"Underground Exploration – Depth 2"
                SetMissionState(4015, 0, 1)
            else:
                pass
        # eventflag:8101:	8101_In-mission branching event flag_dam destruction_betrayal route_ 	8101_ミッション内分岐用イベントフラグ_ダム破壊_裏切りルート_
        elif GetEventFlag(8101) == 1:
            Goto('L0')
        # mission:2230:"Stop the Secret Data Breach"
        elif UnkMissionComplete(2230, 1) == 1:
            Goto('L0')
        # mission:4010:"Underground Exploration – Depth 2"
        elif not UnkMissionComplete(4010, 0) == 1 and not UnkMissionComplete(4010, 1) == 1:
            """State 4"""
            # mission:4010:"Underground Exploration – Depth 2"
            SetMissionState(4010, 0, 1)
        else:
            pass
        """State 5"""
        # mission:4010:"Underground Exploration – Depth 2"
        if UnkMissionComplete(4010, 1) == 1:
            """State 6"""
            Label('L1')
            # mission:4020:"Underground Exploration – Depth 3"
            if not UnkMissionComplete(4020, 0) == 1 and not UnkMissionComplete(4020, 1) == 1:
                """State 7"""
                # mission:4020:"Underground Exploration – Depth 3"
                SetMissionState(4020, 0, 1)
            else:
                pass
            """State 8"""
            # mission:4020:"Underground Exploration – Depth 3"
            if UnkMissionComplete(4020, 1) == 1:
                """State 9"""
                # mission:2211:"Coral Export Denial"
                if UnkMissionComplete(2211, 1) == 1:
                    """State 14"""
                    # mission:7940:"Eliminate V.III"
                    if not UnkMissionComplete(7940, 0) == 1 and not UnkMissionComplete(7940, 1) == 1:
                        """State 15"""
                        # mission:7940:"Eliminate V.III"
                        SetMissionState(7940, 0, 1)
                        # mission:7930:"Intercept the Redguns"
                        SetMissionState(7930, 0, 1)
                        # mission:4110:"Ambush the Vespers"
                        SetMissionState(4110, 0, 1)
                    else:
                        pass
                # mission:7930:"Intercept the Redguns"
                elif not UnkMissionComplete(7930, 0) == 1 and not UnkMissionComplete(7930, 1) == 1:
                    """State 10"""
                    # mission:7930:"Intercept the Redguns"
                    SetMissionState(7930, 0, 1)
                    # mission:4110:"Ambush the Vespers"
                    SetMissionState(4110, 0, 1)
                else:
                    pass
                """State 11"""
                # mission:7930:"Intercept the Redguns"
                if UnkMissionComplete(7930, 1) == 1:
                    """State 16"""
                    Label('L2')
                    # mission:4110:"Ambush the Vespers"
                    if UnkGameCycle() > 1 and UnkMissionComplete(4110, 1) == 1:
                        """State 22"""
                        Label('L3')
                        # mission:4026:"Unknown Territory Survey"
                        if not UnkMissionComplete(4026, 0) == 1 and not UnkMissionComplete(4026, 1) == 1:
                            """State 23"""
                            # mission:4026:"Unknown Territory Survey"
                            SetMissionState(4026, 0, 1)
                        else:
                            pass
                    # mission:7910:"Prevent Corporate Salvage of New Tech"
                    elif UnkGameCycle() > 1 and UnkMissionComplete(7910, 1) == 1:
                        Goto('L3')
                    # mission:4021:"Unknown Territory Survey"
                    elif not UnkMissionComplete(4021, 0) == 1 and not UnkMissionComplete(4021, 1) == 1:
                        """State 17"""
                        # mission:4021:"Unknown Territory Survey"
                        SetMissionState(4021, 0, 1)
                    else:
                        pass
                    """State 18"""
                    # mission:4021:"Unknown Territory Survey"
                    if UnkMissionComplete(4021, 1) == 1:
                        """State 19"""
                        Label('L4')
                        # mission:7940:"Eliminate V.III"
                        if UnkMissionComplete(7940, 1) == 1:
                            """State 20"""
                            # mission:4035:"Reach the Coral Convergence"
                            if not UnkMissionComplete(4035, 0) == 1 and not UnkMissionComplete(4035, 1) == 1:
                                """State 21"""
                                # mission:4035:"Reach the Coral Convergence"
                                SetMissionState(4035, 0, 1)
                            else:
                                pass
                            """State 24"""
                        # mission:4030:"Reach the Coral Convergence"
                        elif not UnkMissionComplete(4030, 0) == 1 and not UnkMissionComplete(4030, 1) == 1:
                            """State 12"""
                            # mission:4030:"Reach the Coral Convergence"
                            SetMissionState(4030, 0, 1)
                        else:
                            pass
                    # mission:4026:"Unknown Territory Survey"
                    elif UnkMissionComplete(4026, 1) == 1:
                        Goto('L4')
                    else:
                        pass
                # mission:4110:"Ambush the Vespers"
                elif UnkMissionComplete(4110, 1) == 1:
                    Goto('L2')
                # mission:7940:"Eliminate V.III"
                elif UnkMissionComplete(7940, 1) == 1:
                    Goto('L2')
                else:
                    pass
            else:
                pass
        # mission:4015:"Underground Exploration – Depth 2"
        elif UnkMissionComplete(4015, 1) == 1:
            Goto('L1')
        else:
            pass
    else:
        pass
    """State 26"""
    return 0

def t001000000_x6():
    """State 0,19"""
    # mission:4035:"Reach the Coral Convergence"
    if UnkMissionComplete(4035, 1) == 1:
        """State 21"""
        # mission:4100:"MIA"
        if not UnkMissionComplete(4100, 0) == 1 and not UnkMissionComplete(4100, 1) == 1:
            """State 27"""
            # mission:4100:"MIA"
            SetMissionState(4100, 0, 1)
        else:
            pass
        """State 20"""
        # mission:4100:"MIA"
        if UnkMissionComplete(4100, 1) == 1:
            """State 5"""
            # mission:5110:"Regain Control of the Xylem"
            SetMissionState(5110, 0, 1)
            # mission:5110:"Regain Control of the Xylem"
            if not UnkMissionComplete(5110, 0) == 1 and not UnkMissionComplete(5110, 1) == 1:
                """State 22"""
                # mission:5110:"Regain Control of the Xylem"
                SetMissionState(5110, 0, 1)
            else:
                pass
            """State 23"""
            # mission:5110:"Regain Control of the Xylem"
            if UnkMissionComplete(5110, 1) == 1:
                """State 7"""
                # mission:6020:"Coral Release"
                if not UnkMissionComplete(6020, 0) == 1 and not UnkMissionComplete(6020, 1) == 1:
                    """State 8"""
                    # mission:6020:"Coral Release"
                    SetMissionState(6020, 0, 1)
                else:
                    pass
            else:
                pass
        else:
            pass
        """State 29"""
        return 1
    # mission:5010:"Take the Uninhabited Floating City"
    elif not UnkMissionComplete(5010, 0) == 1 and not UnkMissionComplete(5010, 1) == 1:
        """State 1"""
        # mission:5010:"Take the Uninhabited Floating City"
        SetMissionState(5010, 0, 1)
    else:
        pass
    """State 26,6"""
    # mission:5010:"Take the Uninhabited Floating City"
    if UnkMissionComplete(5010, 1) == 1:
        """State 2"""
        # mission:5020:"Intercept the Corporate Forces"
        if not UnkMissionComplete(5020, 0) == 1 and not UnkMissionComplete(5020, 1) == 1:
            """State 3"""
            # mission:5020:"Intercept the Corporate Forces"
            SetMissionState(5020, 0, 1)
            # mission:5050:"Eliminate "Cinder" Carla"
            SetMissionState(5050, 0, 1)
        else:
            pass
        """State 4"""
        # mission:5020:"Intercept the Corporate Forces"
        if UnkMissionComplete(5020, 1) == 1:
            """State 24,14"""
            # mission:5040:"Breach the Kármán Line"
            if not UnkMissionComplete(5040, 0) == 1 and not UnkMissionComplete(5040, 1) == 1:
                """State 15"""
                # mission:5040:"Breach the Kármán Line"
                SetMissionState(5040, 0, 1)
            else:
                pass
            """State 16"""
            # mission:5040:"Breach the Kármán Line"
            if UnkMissionComplete(5040, 1) == 1:
                """State 17"""
                # mission:6000:"Shut Down the Closure Satellites"
                assert not UnkMissionComplete(6000, 0) == 1 and not UnkMissionComplete(6000, 1) == 1
                """State 18"""
                # mission:6000:"Shut Down the Closure Satellites"
                SetMissionState(6000, 0, 1)
            else:
                pass
            """State 30"""
            return 2
        # mission:5050:"Eliminate "Cinder" Carla"
        elif UnkMissionComplete(5050, 1) == 1:
            """State 25,9"""
            # mission:5030:"Destroy the Drive Block"
            if not UnkMissionComplete(5030, 0) == 1 and not UnkMissionComplete(5030, 1) == 1:
                """State 10"""
                # mission:5030:"Destroy the Drive Block"
                SetMissionState(5030, 0, 1)
            else:
                pass
            """State 11"""
            # mission:5030:"Destroy the Drive Block"
            if UnkMissionComplete(5030, 1) == 1:
                """State 12"""
                # mission:6010:"Bring Down the Xylem"
                if not UnkMissionComplete(6010, 0) == 1 and not UnkMissionComplete(6010, 1) == 1:
                    """State 13"""
                    # mission:6010:"Bring Down the Xylem"
                    SetMissionState(6010, 0, 1)
                else:
                    pass
            else:
                pass
            """State 28"""
            return 0
    else:
        """State 31"""
        return 3

def t001000000_x7():
    """State 0,4"""
    c1_224(40001)
    # eventflag:3400:	[Garage] Judgment by seeing the story production_Chapter 1 progress 1 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度1
    if UnkGameCycle() > 1 and not GetEventFlag(3400) and not GetChapter():
        """State 5"""
        c1_230(1)
        """State 66"""
        call = t001000000_x15()
        # eventflag:6521:	Obtain parts by clearing the final battle B 	決戦Bクリアでパーツ入手, eventflag:6001:	B route clear 	Bルートクリア
        if call.Done() and (not GetEventFlag(6521) and GetEventFlag(6001) == 1):
            """State 62"""
            # protector:50080000:IB-C03H: HAL 826
            GiveItemDirectly(1, 50080000, 1)
            # protector:51080000:IB-C03C: HAL 826
            GiveItemDirectly(1, 51080000, 1)
            # protector:52080000:IB-C03A: HAL 826
            GiveItemDirectly(1, 52080000, 1)
            # protector:53080000:IB-C03L: HAL 826
            GiveItemDirectly(1, 53080000, 1)
            # eventflag:6521:	Obtain parts by clearing the final battle B 	決戦Bクリアでパーツ入手
            SetEventFlag(6521, 1)
            assert f338() == 1
        elif call.Done():
            pass
        """State 61"""
        # eventflag:6000:	A route clear 	Aルートクリア, eventflag:6001:	B route clear 	Bルートクリア
        if GetEventFlag(6000) == 1 and GetEventFlag(6001) == 1:
            """State 48"""
            ShowGrandioseTextPresentation(90015002)
            assert f320(7) == 1
            """State 118"""
            # talk:910020010:"Looks like you passed the authentication."
            assert t001000000_x33(text3=910020010, z3=91000000)
        else:
            """State 6"""
            ShowGrandioseTextPresentation(90015001)
            assert f320(7) == 1
            """State 75"""
            # talk:910011010:"Looks like you passed the authentication."
            assert t001000000_x33(text3=910011010, z3=91000000)
    # mission:2010:"Illegal Entry", eventflag:3400:	[Garage] Judgment by seeing the story production_Chapter 1 progress 1 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度1
    elif UnkMissionComplete(2010, 1) == 1 and not GetEventFlag(3400):
        """State 1"""
        c1_230(1)
        """State 65"""
        assert t001000000_x15()
        """State 2"""
        ShowGrandioseTextPresentation(90015000)
        assert f320(7) == 1
        """State 74"""
        # talk:910001010:"Looks like you passed the authentication."
        assert t001000000_x33(text3=910001010, z3=91000000)
        """State 90"""
        # talk:910002010:"This notification follows\nrestoral of access privileges."
        assert t001000000_x33(text3=910002010, z3=91000010)
        """State 84"""
        assert t001000000_x30()
        """State 91"""
        assert t001000000_x45()
        """State 73"""
        assert t001000000_x26()
    else:
        """State 19"""
        # mission:7970:"Destroy Artillery Installations", eventflag:3401:	[Garage] Judgment by seeing the story production_Chapter 1 progress 2 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度2
        if UnkMissionComplete(7970, 1) == 1 and not GetEventFlag(3401):
            """State 24"""
            Label('L0')
            c1_230(1)
            if UnkGameCycle() > 1:
                """State 92"""
                # talk:999000000:"No new messages."
                assert t001000000_x46(text1=999000000, z1=91000060)
            else:
                """State 128"""
                # talk:999001000:"One new message."
                assert t001000000_x46(text1=999001000, z1=91000060)
                """State 76"""
                # talk:910300010:"This is a notification from ALLMIND,\nthe mercenary support system."
                assert t001000000_x33(text3=910300010, z3=91000010)
                """State 64"""
                assert t001000000_x8()
                """State 80"""
                assert t001000000_x17()
            """State 25"""
            c1_229(7)
            # eventflag:3401:	[Garage] Judgment by seeing the story production_Chapter 1 progress 2 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度2
            SetEventFlag(3401, 1)
            """State 139"""
            return 5
        # eventflag:3401:	[Garage] Judgment by seeing the story production_Chapter 1 progress 2 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度2, mission:7920:"Grid 135 Cleanup"
        elif not GetEventFlag(3401) and UnkMissionComplete(7920, 1) == 1:
            Goto('L0')
        else:
            """State 26"""
            # mission:7920:"Grid 135 Cleanup", mission:7970:"Destroy Artillery Installations", eventflag:3402:	[Garage] Judgment by seeing the story production_Chapter 1 progress 3 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度3
            if UnkMissionComplete(7920, 1) == 1 and UnkMissionComplete(7970, 1) == 1 and not GetEventFlag(3402):
                """State 21"""
                c1_230(1)
                if UnkGameCycle() > 1:
                    """State 113"""
                    # talk:999000000:"No new messages."
                    assert t001000000_x46(text1=999000000, z1=91000060)
                else:
                    """State 93"""
                    # talk:999001000:"One new message."
                    assert t001000000_x46(text1=999001000, z1=91000060)
                    """State 129"""
                    # talk:910302010:"Registration number Rb23, callsign Raven.\nYour records have been updated."
                    assert t001000000_x33(text3=910302010, z3=91000010)
                    """State 79"""
                    assert t001000000_x34()
                """State 20"""
                # eventflag:3402:	[Garage] Judgment by seeing the story production_Chapter 1 progress 3 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度3
                SetEventFlag(3402, 1)
                """State 138"""
                return 4
            else:
                """State 28"""
                # mission:7900:"Destroy the Transport Helicopters", eventflag:3403:	[Garage] Judgment by seeing the story production_Chapter 1 progress 4 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度4
                if UnkMissionComplete(7900, 1) == 1 and not GetEventFlag(3403):
                    """State 29"""
                    c1_230(1)
                    """State 96"""
                    # talk:999001000:"One new message."
                    assert t001000000_x46(text1=999001000, z1=91000060)
                    """State 97"""
                    # talk:910350010:"I see you're back, 621."
                    assert t001000000_x33(text3=910350010, z3=91000000)
                    """State 31"""
                    # eventflag:3403:	[Garage] Judgment by seeing the story production_Chapter 1 progress 4 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度4
                    SetEventFlag(3403, 1)
                else:
                    """State 33"""
                    # mission:7980:"Destroy the Tester AC", eventflag:3404:	[Garage] Judgment by seeing the story production_Chapter 1 progress 5 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度5
                    if UnkMissionComplete(7980, 1) == 1 and not GetEventFlag(3404):
                        """State 30"""
                        c1_230(1)
                        """State 98"""
                        # talk:999001000:"One new message."
                        assert t001000000_x46(text1=999001000, z1=91000060)
                        """State 99"""
                        # talk:910450010:"621, about the tester AC you downed..."
                        assert t001000000_x33(text3=910450010, z3=91000000)
                        """State 32"""
                        # eventflag:3404:	[Garage] Judgment by seeing the story production_Chapter 1 progress 5 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度5
                        SetEventFlag(3404, 1)
                    else:
                        """State 7"""
                        # eventflag:3406:	[Garage] Judgment by seeing the story production_Chapter 1 progress 7 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度7, eventflag:8101:	8101_In-mission branching event flag_dam destruction_betrayal route_ 	8101_ミッション内分岐用イベントフラグ_ダム破壊_裏切りルート_
                        if not GetEventFlag(3406) and GetEventFlag(8101) == 1:
                            """State 10"""
                            c1_230(1)
                            """State 68"""
                            assert t001000000_x15()
                            """State 95"""
                            # talk:999001000:"One new message."
                            assert t001000000_x46(text1=999001000, z1=91000060)
                            """State 87"""
                            # talk:911160010:"...Tch."
                            assert t001000000_x33(text3=911160010, z3=91000050)
                            """State 9"""
                            Label('L1')
                            c1_229(7)
                            UnkUnlockDecal(6614)
                            # mission:2080:"Destroy the Weaponized Mining Ship"
                            if UnkMissionComplete(2080, 1) == 1 and f338() == 1:
                                """State 36"""
                                Label('L2')
                                # eventflag:3407:	[Garage] Judgment by seeing the story production_Chapter 1 progress 8 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度8
                                SetEventFlag(3407, 1)
                                # eventflag:3406:	[Garage] Judgment by seeing the story production_Chapter 1 progress 7 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度7
                                SetEventFlag(3406, 1)
                            # mission:2250:"Escort the Weaponized Mining Ship"
                            elif UnkMissionComplete(2250, 1) == 1 and f338() == 1:
                                Goto('L2')
                            elif f338() == 1:
                                """State 141"""
                                # eventflag:3406:	[Garage] Judgment by seeing the story production_Chapter 1 progress 7 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度7
                                SetEventFlag(3406, 1)
                                return 7
                        # mission:2025:"Attack the Dam Complex", eventflag:3406:	[Garage] Judgment by seeing the story production_Chapter 1 progress 7 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度7
                        elif UnkMissionComplete(2025, 1) == 1 and not GetEventFlag(3406):
                            """State 8"""
                            Label('L3')
                            c1_230(1)
                            """State 67"""
                            assert t001000000_x15()
                            """State 94"""
                            # talk:999001000:"One new message."
                            assert t001000000_x46(text1=999001000, z1=91000060)
                            """State 86"""
                            # talk:911150010:"...Tch."
                            assert t001000000_x33(text3=911150010, z3=91000050)
                            Goto('L1')
                        # mission:2020:"Attack the Dam Complex", eventflag:3406:	[Garage] Judgment by seeing the story production_Chapter 1 progress 7 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度7
                        elif UnkMissionComplete(2020, 1) == 1 and not GetEventFlag(3406):
                            Goto('L3')
                        else:
                            """State 27"""
                            # mission:2080:"Destroy the Weaponized Mining Ship", eventflag:3407:	[Garage] Judgment by seeing the story production_Chapter 1 progress 8 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度8
                            if UnkMissionComplete(2080, 1) == 1 and not GetEventFlag(3407):
                                """State 34"""
                                c1_230(1)
                                """State 100"""
                                assert t001000000_x15()
                                """State 101"""
                                # talk:999001000:"One new message."
                                assert t001000000_x46(text1=999001000, z1=91000060)
                                """State 102"""
                                # talk:911250010:"Raven. Your work on the STRIDER\ndeserves commendation."
                                assert t001000000_x33(text3=911250010, z3=91000070)
                            else:
                                """State 49"""
                                # mission:2250:"Escort the Weaponized Mining Ship", eventflag:3407:	[Garage] Judgment by seeing the story production_Chapter 1 progress 8 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度8
                                if UnkMissionComplete(2250, 1) == 1 and not GetEventFlag(3407):
                                    """State 50"""
                                    c1_230(1)
                                    """State 119"""
                                    assert t001000000_x15()
                                    """State 120"""
                                    # talk:999001000:"One new message."
                                    assert t001000000_x46(text1=999001000, z1=91000060)
                                    """State 121"""
                                    # talk:911270010:"...Raven. First up, let me apologize."
                                    assert t001000000_x33(text3=911270010, z3=91000090)
                                else:
                                    """State 11"""
                                    # eventflag:3408:	[Garage] Judgment by seeing the story production_Chapter 1 progress 9 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度9, mission:2080:"Destroy the Weaponized Mining Ship", mission:2020:"Attack the Dam Complex"
                                    if (not GetEventFlag(3408) and UnkMissionComplete(2080, 1) == 1 and
                                        UnkMissionComplete(2020, 1) == 1 and UnkGameCycle() <= 1):
                                        Goto('L12')
                                    # mission:2250:"Escort the Weaponized Mining Ship", mission:2025:"Attack the Dam Complex", eventflag:3408:	[Garage] Judgment by seeing the story production_Chapter 1 progress 9 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度9
                                    elif (UnkMissionComplete(2250, 1) == 1 and UnkMissionComplete(2025,
                                          1) == 1 and not GetEventFlag(3408)):
                                        Goto('L12')
                                    # mission:2025:"Attack the Dam Complex", mission:2080:"Destroy the Weaponized Mining Ship", eventflag:3408:	[Garage] Judgment by seeing the story production_Chapter 1 progress 9 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度9
                                    elif (UnkMissionComplete(2025, 1) == 1 and UnkMissionComplete(2080,
                                          1) == 1 and not GetEventFlag(3408)):
                                        Goto('L12')
                                    else:
                                        """State 14"""
                                        # eventflag:3450:	[Garage] Judgment by seeing the story production_Chapter 1 progress 10 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度10, mission:2030:"Operation Wallclimber", eventflag:8101:	8101_In-mission branching event flag_dam destruction_betrayal route_ 	8101_ミッション内分岐用イベントフラグ_ダム破壊_裏切りルート_
                                        if (not GetEventFlag(3450) and UnkMissionComplete(2030, 1) ==
                                            1 and UnkGameCycle() > 1 and GetEventFlag(8101) == 1):
                                            """State 17"""
                                            c1_230(1)
                                            """State 70"""
                                            assert t001000000_x15()
                                            """State 126"""
                                            # talk:999001000:"One new message."
                                            assert t001000000_x46(text1=999001000, z1=91000060)
                                            """State 78"""
                                            # talk:913010010:"We're war buddies now.\nI think I should tell you something."
                                            assert t001000000_x33(text3=913010010, z3=91000020)
                                        # eventflag:3450:	[Garage] Judgment by seeing the story production_Chapter 1 progress 10 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度10, mission:2030:"Operation Wallclimber"
                                        elif not GetEventFlag(3450) and UnkMissionComplete(2030, 1) == 1:
                                            """State 15"""
                                            c1_230(1)
                                            """State 69"""
                                            call = t001000000_x15()
                                            if call.Done() and UnkGameCycle() > 1:
                                                """State 104"""
                                                # talk:999001000:"One new message."
                                                assert t001000000_x46(text1=999001000, z1=91000060)
                                                """State 105"""
                                                # talk:913000010:"We're war buddies now.\nI think I should tell you something."
                                                assert t001000000_x33(text3=913000010, z3=91000020)
                                            elif call.Done():
                                                """State 103"""
                                                # talk:999001000:"One new message."
                                                assert t001000000_x46(text1=999001000, z1=91000060)
                                                """State 77"""
                                                # talk:913000010:"We're war buddies now.\nI think I should tell you something."
                                                assert t001000000_x33(text3=913000010, z3=91000020)
                                                """State 83"""
                                                assert t001000000_x32()
                                                """State 72"""
                                                assert t001000000_x19()
                                        else:
                                            """State 18"""
                                            # mission:2100:"Retrieve Combat Logs", eventflag:3451:	[Garage] Judgment by seeing the story production_Chapter 1 progress 11 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度11
                                            if UnkMissionComplete(2100, 1) == 1 and not GetEventFlag(3451):
                                                """State 22"""
                                                c1_230(1)
                                                """State 88"""
                                                call = t001000000_x15()
                                                # mission:2060:"Investigate BAWS Arsenal No. 2"
                                                if call.Done() and UnkMissionComplete(2060, 1) == 1:
                                                    """State 41"""
                                                    Label('L4')
                                                    """State 110"""
                                                    # talk:999002000:"Two new messages."
                                                    assert t001000000_x46(text1=999002000, z1=91000060)
                                                # mission:2200:"Obstruct the Mandatory Inspection"
                                                elif call.Done() and UnkMissionComplete(2200, 1) == 1:
                                                    Goto('L4')
                                                # eventflag:3131:	OS_Update_Unban 	OS_Update_解禁用
                                                elif call.Done() and not GetEventFlag(3131):
                                                    """State 106"""
                                                    # talk:999002000:"Two new messages."
                                                    assert t001000000_x46(text1=999002000, z1=91000060)
                                                elif call.Done():
                                                    """State 132"""
                                                    # talk:999001000:"One new message."
                                                    assert t001000000_x46(text1=999001000, z1=91000060)
                                                """State 89"""
                                                # talk:913150010:"G13 Raven!"
                                                assert t001000000_x33(text3=913150010, z3=91000080)
                                                """State 58"""
                                                UnkUnlockDecal(6607)
                                                assert f338() == 1
                                                """State 59"""
                                                # eventflag:3131:	OS_Update_Unban 	OS_Update_解禁用
                                                if not GetEventFlag(3131):
                                                    """State 85"""
                                                    # talk:913001010:"Registration number Rb23, callsign Raven.\nYour records have been updated."
                                                    assert t001000000_x33(text3=913001010, z3=91000010)
                                                    """State 82"""
                                                    assert t001000000_x10()
                                                    """State 23"""
                                                    Label('L5')
                                                    # eventflag:3451:	[Garage] Judgment by seeing the story production_Chapter 1 progress 11 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度11
                                                    SetEventFlag(3451, 1)
                                                    c1_229(7)
                                                else:
                                                    Goto('L5')
                                            else:
                                                """State 45"""
                                                # mission:2140:"Prisoner Rescue", eventflag:3451:	[Garage] Judgment by seeing the story production_Chapter 1 progress 11 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度11
                                                if UnkMissionComplete(2140, 1) == 1 and not GetEventFlag(3451):
                                                    """State 46"""
                                                    c1_230(1)
                                                    """State 114"""
                                                    call = t001000000_x15()
                                                    # mission:2060:"Investigate BAWS Arsenal No. 2"
                                                    if call.Done() and UnkMissionComplete(2060, 1) == 1:
                                                        """State 47"""
                                                        Label('L6')
                                                        """State 117"""
                                                        # talk:999002000:"Two new messages."
                                                        assert t001000000_x46(text1=999002000, z1=91000060)
                                                        """State 127"""
                                                        # talk:913160010:"Let me thank you again, Raven."
                                                        assert t001000000_x33(text3=913160010, z3=91000090)
                                                        Goto('L5')
                                                    # mission:2200:"Obstruct the Mandatory Inspection"
                                                    elif (call.Done() and UnkMissionComplete(2200, 1)
                                                          == 1):
                                                        Goto('L6')
                                                    elif call.Done():
                                                        """State 115"""
                                                        # talk:999001000:"One new message."
                                                        assert t001000000_x46(text1=999001000, z1=91000060)
                                                        """State 116"""
                                                        # talk:913160010:"Let me thank you again, Raven."
                                                        assert t001000000_x33(text3=913160010, z3=91000090)
                                                        Goto('L5')
                                                    """State 39"""
                                                    Label('L7')
                                                    # eventflag:3452:	[Garage] Judgment by seeing the story production_Chapter 1 progress 12 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度12
                                                    SetEventFlag(3452, 1)
                                                    c1_229(7)
                                                else:
                                                    """State 37"""
                                                    # mission:2060:"Investigate BAWS Arsenal No. 2", eventflag:3452:	[Garage] Judgment by seeing the story production_Chapter 1 progress 12 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度12
                                                    if UnkMissionComplete(2060, 1) == 1 and not GetEventFlag(3452):
                                                        """State 38"""
                                                        c1_230(1)
                                                        """State 107"""
                                                        call = t001000000_x15()
                                                        # eventflag:3131:	OS_Update_Unban 	OS_Update_解禁用
                                                        if call.Done() and not GetEventFlag(3131):
                                                            """State 133"""
                                                            # talk:999002000:"Two new messages."
                                                            assert t001000000_x46(text1=999002000, z1=91000060)
                                                        elif call.Done():
                                                            """State 109"""
                                                            # talk:999001000:"One new message."
                                                            call = t001000000_x46(text1=999001000, z1=91000060)
                                                            # mission:2100:"Retrieve Combat Logs"
                                                            if (call.Done() and UnkMissionComplete(2100,
                                                                1) == 1):
                                                                """State 42"""
                                                                Label('L8')
                                                                """State 111"""
                                                                # talk:913201010:"I see you're back, 621."
                                                                assert t001000000_x33(text3=913201010, z3=91000000)
                                                                """State 43"""
                                                                # eventflag:3453:	[Garage] Judgment by seeing the story production_Chapter 1 progress 13 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度13
                                                                SetEventFlag(3453, 1)
                                                                c1_229(7)
                                                                # eventflag:3452:	[Garage] Judgment by seeing the story production_Chapter 1 progress 12 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度12
                                                                SetEventFlag(3452, 1)
                                                                """State 142"""
                                                                return 8
                                                            # mission:2140:"Prisoner Rescue"
                                                            elif (call.Done() and UnkMissionComplete(2140,
                                                                  1) == 1):
                                                                Goto('L8')
                                                            elif call.Done():
                                                                pass
                                                        """State 108"""
                                                        # talk:913200010:"I see you're back, 621."
                                                        assert t001000000_x33(text3=913200010, z3=91000000)
                                                        """State 60"""
                                                        # eventflag:3131:	OS_Update_Unban 	OS_Update_解禁用
                                                        if not GetEventFlag(3131):
                                                            """State 130"""
                                                            # talk:913001010:"Registration number Rb23, callsign Raven.\nYour records have been updated."
                                                            assert t001000000_x33(text3=913001010, z3=91000010)
                                                            """State 131"""
                                                            assert t001000000_x10()
                                                            Goto('L7')
                                                        else:
                                                            Goto('L7')
                                                    else:
                                                        """State 52"""
                                                        # mission:2200:"Obstruct the Mandatory Inspection", eventflag:3452:	[Garage] Judgment by seeing the story production_Chapter 1 progress 12 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度12
                                                        if (UnkMissionComplete(2200, 1) == 1 and not
                                                            GetEventFlag(3452)):
                                                            """State 51"""
                                                            c1_230(1)
                                                            """State 122"""
                                                            call = t001000000_x15()
                                                            # mission:2140:"Prisoner Rescue"
                                                            if (call.Done() and UnkMissionComplete(2140,
                                                                1) == 1):
                                                                """State 53"""
                                                                Label('L9')
                                                                """State 123"""
                                                                # talk:999002000:"Two new messages."
                                                                assert t001000000_x46(text1=999002000, z1=91000060)
                                                            # mission:2100:"Retrieve Combat Logs"
                                                            elif (call.Done() and UnkMissionComplete(2100,
                                                                  1) == 1):
                                                                Goto('L9')
                                                            elif call.Done():
                                                                """State 125"""
                                                                # talk:999001000:"One new message."
                                                                assert t001000000_x46(text1=999001000, z1=91000060)
                                                            """State 124"""
                                                            # talk:913220010:"Raven.\nThanks for the help with the mission."
                                                            call = t001000000_x33(text3=913220010, z3=91000110)
                                                            # eventflag:3453:	[Garage] Judgment by seeing the story production_Chapter 1 progress 13 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度13, mission:2140:"Prisoner Rescue", mission:2200:"Obstruct the Mandatory Inspection"
                                                            if (call.Done() and (not GetEventFlag(3453) and
                                                                UnkMissionComplete(2140, 1) == 1 and UnkMissionComplete(2200,
                                                                1) == 1)):
                                                                """State 57"""
                                                                Label('L10')
                                                                """State 63"""
                                                                UnkUnlockDecal(6611)
                                                                assert f338() == 1
                                                                Goto('L7')
                                                            # eventflag:3453:	[Garage] Judgment by seeing the story production_Chapter 1 progress 13 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度13, mission:2100:"Retrieve Combat Logs", mission:2060:"Investigate BAWS Arsenal No. 2"
                                                            elif (call.Done() and (not GetEventFlag(3453) and
                                                                  UnkMissionComplete(2100, 1) == 1 and UnkMissionComplete(2060,
                                                                  1) == 1)):
                                                                Goto('L10')
                                                            # eventflag:3453:	[Garage] Judgment by seeing the story production_Chapter 1 progress 13 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度13, mission:2140:"Prisoner Rescue", mission:2200:"Obstruct the Mandatory Inspection"
                                                            elif (call.Done() and (not GetEventFlag(3453) and
                                                                  UnkMissionComplete(2140, 1) == 1 and UnkMissionComplete(2200,
                                                                  1) == 1)):
                                                                Goto('L10')
                                                            # mission:2200:"Obstruct the Mandatory Inspection", mission:2100:"Retrieve Combat Logs", eventflag:3453:	[Garage] Judgment by seeing the story production_Chapter 1 progress 13 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度13
                                                            elif (call.Done() and (UnkMissionComplete(2200,
                                                                  1) == 1 and UnkMissionComplete(2100, 1) ==
                                                                  1 and not GetEventFlag(3453))):
                                                                Goto('L10')
                                                            # eventflag:3453:	[Garage] Judgment by seeing the story production_Chapter 1 progress 13 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度13, mission:2140:"Prisoner Rescue", mission:2060:"Investigate BAWS Arsenal No. 2"
                                                            elif (call.Done() and (not GetEventFlag(3453) and
                                                                  UnkMissionComplete(2140, 1) == 1 and UnkMissionComplete(2060,
                                                                  1) == 1)):
                                                                Goto('L10')
                                                            elif call.Done():
                                                                """State 56"""
                                                                UnkUnlockDecal(6611)
                                                                assert f338() == 1
                                                                Goto('L7')
                                                        else:
                                                            pass
                                            """State 40"""
                                            # eventflag:3453:	[Garage] Judgment by seeing the story production_Chapter 1 progress 13 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度13, mission:2140:"Prisoner Rescue", mission:2200:"Obstruct the Mandatory Inspection"
                                            if (not GetEventFlag(3453) and UnkMissionComplete(2140, 1)
                                                == 1 and UnkMissionComplete(2200, 1) == 1):
                                                """State 112"""
                                                Label('L11')
                                                # talk:914100010:"...Got a job for you, 621."
                                                assert t001000000_x33(text3=914100010, z3=91000000)
                                                """State 44"""
                                                c1_229(7)
                                                """State 143"""
                                                # eventflag:3453:	[Garage] Judgment by seeing the story production_Chapter 1 progress 13 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度13
                                                SetEventFlag(3453, 1)
                                                return 9
                                            # eventflag:3453:	[Garage] Judgment by seeing the story production_Chapter 1 progress 13 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度13, mission:2100:"Retrieve Combat Logs", mission:2060:"Investigate BAWS Arsenal No. 2"
                                            elif (not GetEventFlag(3453) and UnkMissionComplete(2100,
                                                  1) == 1 and UnkMissionComplete(2060, 1) == 1):
                                                Goto('L11')
                                            # eventflag:3453:	[Garage] Judgment by seeing the story production_Chapter 1 progress 13 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度13, mission:2140:"Prisoner Rescue", mission:2200:"Obstruct the Mandatory Inspection"
                                            elif (not GetEventFlag(3453) and UnkMissionComplete(2140,
                                                  1) == 1 and UnkMissionComplete(2200, 1) == 1):
                                                Goto('L11')
                                            # mission:2200:"Obstruct the Mandatory Inspection", mission:2100:"Retrieve Combat Logs", eventflag:3453:	[Garage] Judgment by seeing the story production_Chapter 1 progress 13 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度13
                                            elif (UnkMissionComplete(2200, 1) == 1 and UnkMissionComplete(2100,
                                                  1) == 1 and not GetEventFlag(3453)):
                                                Goto('L11')
                                            # eventflag:3453:	[Garage] Judgment by seeing the story production_Chapter 1 progress 13 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度13, mission:2140:"Prisoner Rescue", mission:2060:"Investigate BAWS Arsenal No. 2"
                                            elif (not GetEventFlag(3453) and UnkMissionComplete(2140,
                                                  1) == 1 and UnkMissionComplete(2060, 1) == 1):
                                                Goto('L11')
                                            else:
                                                """State 134"""
                                                c1_230(0)
                                                return 0
                                        """State 16"""
                                        # eventflag:3450:	[Garage] Judgment by seeing the story production_Chapter 1 progress 10 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度10
                                        SetEventFlag(3450, 1)
                                        c1_229(7)
                                        """State 137"""
                                        c1_230(0)
                                        return 3
                            """State 35"""
                            c1_229(7)
                            UnkUnlockDecal(6605)
                            # mission:2020:"Attack the Dam Complex"
                            if UnkMissionComplete(2020, 1) == 1 and f338() == 1:
                                Goto('L2')
                            # mission:2025:"Attack the Dam Complex"
                            elif UnkMissionComplete(2025, 1) == 1 and f338() == 1:
                                Goto('L2')
                            elif f338() == 1:
                                """State 144"""
                                # eventflag:3407:	[Garage] Judgment by seeing the story production_Chapter 1 progress 8 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度8
                                SetEventFlag(3407, 1)
                                return 10
                        """State 12"""
                        Label('L12')
                        c1_230(1)
                        if UnkGameCycle() > 1:
                            pass
                        else:
                            """State 81"""
                            assert t001000000_x18()
                            """State 71"""
                            assert t001000000_x16()
                        """State 13"""
                        c1_229(7)
                        if True:
                            """State 54"""
                            UnkUnlockDecal(6605)
                            """State 55"""
                            UnkUnlockDecal(6614)
                        else:
                            pass
                        """State 136"""
                        c1_230(0)
                        # eventflag:3408:	[Garage] Judgment by seeing the story production_Chapter 1 progress 9 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度9
                        SetEventFlag(3408, 1)
                        return 2
                """State 140"""
                return 6
    """State 3"""
    # eventflag:3400:	[Garage] Judgment by seeing the story production_Chapter 1 progress 1 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度1
    SetEventFlag(3400, 1)
    c1_229(7)
    """State 135"""
    c1_230(0)
    return 1

def t001000000_x8():
    """State 0,1"""
    # eventflag:3127:	Market_Unlocking 	Market_解禁用
    SetEventFlag(3127, 1)
    c1_230(0)
    c1_229(7)
    # eventflag:6200:	Chapter 1 beginning submi x 2 	１章冒頭サブミ×２
    SetEventFlag(6200, 1)
    """State 2,3"""
    # tutorial:2100000:Access Granted: PARTS SHOP
    ShowTutorialMessage(2100000)
    assert (not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            and GetCurrentStateElapsedFrames() > 1)
    """State 4"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    return 0

def t001000000_x9():
    """State 0,1"""
    c1_224(50030)
    # eventflag:3410:	[Garage] Judgment by seeing the story production_Chapter 2 progress 1 	【ガレージ】ストーリー演出を見た判定_チャプター2進行度1
    if not GetEventFlag(3410):
        pass
    else:
        Goto('L0')
    """State 3,13"""
    call = t001000000_x15()
    if call.Done() and (UnkGameCycle() > 2 and f320(7) == 1):
        """State 27"""
        # talk:999008000:"Augmented human C4-621: Entering Standard Mode."
        assert t001000000_x46(text1=999008000, z1=91000060)
        """State 28"""
        # talk:920000010:"621. I've got some business to attend to."
        assert t001000000_x33(text3=920000010, z3=91000000)
        """State 29"""
        # talk:920001010:"...Raven."
        assert t001000000_x33(text3=920001010, z3=91000030)
        """State 11"""
    # eventflag:3156:	Arena unlock progress 7 	アリーナ解禁進行度7
    elif call.Done() and (UnkGameCycle() > 1 and f320(7) == 1 and not GetEventFlag(3156)):
        """State 24"""
        # talk:999009000:"Augmented human C4-621: Entering Standard Mode."
        assert t001000000_x46(text1=999009000, z1=91000060)
        """State 25"""
        # talk:920000010:"621. I've got some business to attend to."
        assert t001000000_x33(text3=920000010, z3=91000000)
        """State 26"""
        # talk:920001010:"...Raven."
        assert t001000000_x33(text3=920001010, z3=91000030)
        """State 21"""
        # talk:920010010:"Registration number Rb23, callsign Raven."
        assert t001000000_x33(text3=920010010, z3=91000010)
        """State 22"""
        assert t001000000_x28()
    elif call.Done():
        """State 23"""
        # talk:999009000:"Augmented human C4-621: Entering Standard Mode."
        assert t001000000_x46(text1=999009000, z1=91000060)
        """State 16"""
        # talk:920000010:"621. I've got some business to attend to."
        assert t001000000_x33(text3=920000010, z3=91000000)
        """State 17"""
        # talk:920001010:"...Raven."
        assert t001000000_x33(text3=920001010, z3=91000030)
        """State 35"""
        # talk:920002010:"Registration number Rb23, callsign Raven.\nYour records have been updated."
        assert t001000000_x33(text3=920002010, z3=91000010)
        """State 20"""
        assert t001000000_x10()
        """State 14"""
        assert t001000000_x20()
    """State 2"""
    # eventflag:3410:	[Garage] Judgment by seeing the story production_Chapter 2 progress 1 	【ガレージ】ストーリー演出を見た判定_チャプター2進行度1
    SetEventFlag(3410, 1)
    c1_229(7)
    """State 40"""
    c1_230(0)
    return 1
    """State 8"""
    Label('L0')
    # eventflag:3411:	[Garage] Judgment by seeing the story production_Chapter 2 progress 2 	【ガレージ】ストーリー演出を見た判定_チャプター2進行度2, mission:2120:"Infiltrate Grid 086"
    if not GetEventFlag(3411) and UnkMissionComplete(2120, 1) == 1:
        pass
    else:
        Goto('L2')
    """State 9,15"""
    call = t001000000_x15()
    # mission:2250:"Escort the Weaponized Mining Ship"
    if call.Done() and UnkMissionComplete(2250, 1) == 1:
        """State 36"""
        Label('L1')
        # talk:999001000:"One new message."
        assert t001000000_x46(text1=999001000, z1=91000060)
        """State 37"""
        # talk:920220010:"Hey tourist! It's me, Carla."
        assert t001000000_x33(text3=920220010, z3=91000040)
        """State 38"""
        # talk:920220020:"...Raven. It's highly unusual to receive\nmessages from hostile sources."
        assert t001000000_x33(text3=920220020, z3=91000030)
    # eventflag:8101:	8101_In-mission branching event flag_dam destruction_betrayal route_ 	8101_ミッション内分岐用イベントフラグ_ダム破壊_裏切りルート_
    elif call.Done() and GetEventFlag(8101) == 1:
        Goto('L1')
    elif call.Done():
        """State 30"""
        # talk:999000000:"No new messages."
        assert t001000000_x46(text1=999000000, z1=91000060)
        """State 18"""
        # talk:920200010:"Raven. We've received a job\nfrom RaD's leader, Carla."
        assert t001000000_x33(text3=920200010, z3=91000030)
    """State 10"""
    # eventflag:3411:	[Garage] Judgment by seeing the story production_Chapter 2 progress 2 	【ガレージ】ストーリー演出を見た判定_チャプター2進行度2
    SetEventFlag(3411, 1)
    c1_229(7)
    """State 41"""
    c1_230(0)
    return 2
    """State 4"""
    Label('L2')
    # eventflag:3412:	[Garage] Judgment by seeing the story production_Chapter 2 progress 3 	【ガレージ】ストーリー演出を見た判定_チャプター2進行度3, mission:7960:"Eliminate the Doser Faction"
    if not GetEventFlag(3412) and UnkMissionComplete(7960, 1) == 1:
        """State 5,32"""
        # talk:999001000:"One new message."
        assert t001000000_x46(text1=999001000, z1=91000060)
        """State 31"""
        # talk:921000010:"Guess you noticed that job from Balam...\nand decided to take it."
        assert t001000000_x33(text3=921000010, z3=91000000)
    # eventflag:3412:	[Garage] Judgment by seeing the story production_Chapter 2 progress 3 	【ガレージ】ストーリー演出を見た判定_チャプター2進行度3, mission:2230:"Stop the Secret Data Breach"
    elif not GetEventFlag(3412) and UnkMissionComplete(2230, 1) == 1:
        """State 7,33"""
        # talk:999001000:"One new message."
        assert t001000000_x46(text1=999001000, z1=91000060)
        """State 34"""
        # talk:921020010:"Guess you noticed that job from Balam...\nand decided to take it."
        call = t001000000_x33(text3=921020010, z3=91000000)
        # mission:2250:"Escort the Weaponized Mining Ship"
        if call.Done() and UnkMissionComplete(2250, 1) == 1:
            """State 19"""
            # talk:921021010:"...Raven. I've managed to decode\nthose encrypted comms."
            assert t001000000_x33(text3=921021010, z3=91000030)
        elif call.Done():
            """State 12"""
            pass
    else:
        """State 39"""
        return 0
    """State 6"""
    # eventflag:3412:	[Garage] Judgment by seeing the story production_Chapter 2 progress 3 	【ガレージ】ストーリー演出を見た判定_チャプター2進行度3
    SetEventFlag(3412, 1)
    c1_229(7)
    """State 42"""
    c1_230(0)
    return 3

def t001000000_x10():
    """State 0,6"""
    c1_229(7)
    # eventflag:3130:	AC_Arena_Unban 	AC_Arena_解禁用
    if not GetEventFlag(3130):
        """State 1"""
        # eventflag:3130:	AC_Arena_Unban 	AC_Arena_解禁用
        SetEventFlag(3130, 1)
        # eventflag:3131:	OS_Update_Unban 	OS_Update_解禁用
        SetEventFlag(3131, 1)
        """State 2,3"""
        # tutorial:2101000:Access Granted: OS TUNING/ARENA
        ShowTutorialMessage(2101000)
        assert (not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
                and GetCurrentStateElapsedFrames() > 1)
        """State 5"""
        c1_252()
        assert (not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
                and GetCurrentStateElapsedFrames() > 1)
        """State 4"""
        assert GetCurrentStateElapsedFrames() > 1
    # eventflag:3150:	Arena unlock progress 1 	アリーナ解禁進行度1
    elif not GetEventFlag(3150):
        """State 7"""
        # eventflag:3150:	Arena unlock progress 1 	アリーナ解禁進行度1
        SetEventFlag(3150, 1)
        """State 8,9"""
        # tutorial:2101010:Data Registry Updated: ARENA
        ShowTutorialMessage(2101010)
        assert (not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
                and GetCurrentStateElapsedFrames() > 1)
        """State 10"""
        assert GetCurrentStateElapsedFrames() > 1
    # mission:2180:"Ocean Crossing", eventflag:3151:	Arena unlock progress 2 	アリーナ解禁進行度2
    elif UnkMissionComplete(2180, 1) == 1 and not GetEventFlag(3151):
        """State 11"""
        # eventflag:3151:	Arena unlock progress 2 	アリーナ解禁進行度2
        SetEventFlag(3151, 1)
        # eventflag:3133:	ONLINE_Arena_Unlocking 	ONLINE_Arena_解禁用
        SetEventFlag(3133, 1)
        """State 12,13"""
        # tutorial:2101010:Data Registry Updated: ARENA
        ShowTutorialMessage(2101010)
        assert (not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
                and GetCurrentStateElapsedFrames() > 1)
        """State 14,15"""
        # tutorial:2101010:Data Registry Updated: ARENA
        ShowTutorialMessage(2101010)
        assert (not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
                and GetCurrentStateElapsedFrames() > 1)
        """State 16"""
        assert GetCurrentStateElapsedFrames() > 1
    # eventflag:3152:	Arena unlock progress 3 	アリーナ解禁進行度3
    elif not GetEventFlag(3152):
        """State 17"""
        # eventflag:3152:	Arena unlock progress 3 	アリーナ解禁進行度3
        SetEventFlag(3152, 1)
        """State 18"""
        # tutorial:2101010:Data Registry Updated: ARENA
        ShowTutorialMessage(2101010)
        assert (not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
                and GetCurrentStateElapsedFrames() > 1)
        """State 19"""
        assert GetCurrentStateElapsedFrames() > 1
    # mission:3043:"Attack the Old Spaceport", eventflag:3153:	Arena unlock progress 4 	アリーナ解禁進行度4
    elif UnkMissionComplete(3043, 1) == 1 and not GetEventFlag(3153):
        """State 20"""
        # eventflag:3153:	Arena unlock progress 4 	アリーナ解禁進行度4
        SetEventFlag(3153, 1)
        """State 21"""
        # tutorial:2101010:Data Registry Updated: ARENA
        ShowTutorialMessage(2101010)
        assert (not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
                and GetCurrentStateElapsedFrames() > 1)
        """State 22"""
        assert GetCurrentStateElapsedFrames() > 1
    # eventflag:3154:	Arena unlock progress 5 	アリーナ解禁進行度5, mission:3230:"Destroy the Ice Worm"
    elif not GetEventFlag(3154) and UnkMissionComplete(3230, 1) == 1:
        """State 23"""
        # eventflag:3154:	Arena unlock progress 5 	アリーナ解禁進行度5
        SetEventFlag(3154, 1)
        """State 24"""
        # tutorial:2101010:Data Registry Updated: ARENA
        ShowTutorialMessage(2101010)
        assert (not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
                and GetCurrentStateElapsedFrames() > 1)
        """State 25"""
        assert GetCurrentStateElapsedFrames() > 1
    # eventflag:4020:	Archive Item Obtained Flag 20 	アーカイブアイテム取得済みフラグ20, mission:3043:"Attack the Old Spaceport"
    elif not GetEventFlag(4020) and UnkMissionComplete(3043, 1) == 1:
        """State 26"""
        # eventflag:3155:	Arena unlock progress 6 	アリーナ解禁進行度6
        SetEventFlag(3155, 1)
        """State 27"""
        # tutorial:2101010:Data Registry Updated: ARENA
        ShowTutorialMessage(2101010)
        assert (not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
                and GetCurrentStateElapsedFrames() > 1)
        """State 28"""
        assert GetCurrentStateElapsedFrames() > 1
    else:
        """State 29"""
        pass
    """State 30"""
    return 0

def t001000000_x11():
    """State 0,1"""
    c1_224(40001)
    # eventflag:3420:	[Garage] Judgment by watching the story production Chapter 3 progress 1 	【ガレージ】ストーリー演出を見た判定チャプター3進行度1
    if not GetEventFlag(3420):
        pass
    else:
        Goto('L0')
    """State 2,80"""
    call = t001000000_x15()
    if call.Done() and UnkGameCycle() > 1:
        """State 104"""
        # talk:999008000:"Augmented human C4-621: Entering Standard Mode."
        assert t001000000_x46(text1=999008000, z1=91000060)
        """State 168"""
        # talk:930000010:"Looks like you've made it\nto the Central Ice Field, 621."
        call = t001000000_x33(text3=930000010, z3=91000000)
        # eventflag:6000:	A route clear 	Aルートクリア, eventflag:6001:	B route clear 	Bルートクリア
        if call.Done() and (GetEventFlag(6000) == 1 and GetEventFlag(6001) == 1):
            """State 17"""
            # eventflag:6015:	Arena unlocking progress 6 take over 	アリーナ解禁進行度6　引継ぎ
            if not GetEventFlag(6015):
                """State 86"""
                # talk:930020010:"Raven."
                assert t001000000_x33(text3=930020010, z3=91000030)
                """State 100"""
                assert t001000000_x42()
            else:
                pass
        # eventflag:6275:	Continental crust: 2nd lap 	大陸殻：２周目
        elif call.Done() and not GetEventFlag(6275):
            """State 178"""
            assert t001000000_x24()
        elif call.Done():
            pass
    elif call.Done():
        """State 103"""
        # talk:999009000:"Augmented human C4-621: Entering Standard Mode."
        assert t001000000_x46(text1=999009000, z1=91000060)
        """State 84"""
        # talk:930000010:"Looks like you've made it\nto the Central Ice Field, 621."
        assert t001000000_x33(text3=930000010, z3=91000000) and UnkGameCycle() <= 1
        """State 85"""
        # talk:930001010:"Registration number Rb23, callsign Raven.\nYour records have been updated."
        assert t001000000_x33(text3=930001010, z3=91000010)
        """State 81"""
        assert t001000000_x10()
        """State 93"""
        # talk:930002010:"Raven."
        assert t001000000_x33(text3=930002010, z3=91000030)
        """State 167"""
        assert t001000000_x47()
        """State 83"""
        assert t001000000_x21()
    """State 7"""
    # eventflag:3420:	[Garage] Judgment by watching the story production Chapter 3 progress 1 	【ガレージ】ストーリー演出を見た判定チャプター3進行度1
    SetEventFlag(3420, 1)
    c1_229(7)
    """State 182"""
    c1_230(0)
    return 1
    """State 3"""
    Label('L0')
    # eventflag:3421:	[Garage] Judgment by seeing the story production Chapter 3 progress 2 	【ガレージ】ストーリー演出を見た判定チャプター3進行度2, mission:3011:"Steal the Survey Data"
    if not GetEventFlag(3421) and UnkMissionComplete(3011, 1) == 1:
        pass
    else:
        Goto('L1')
    """State 4,82"""
    assert t001000000_x15()
    """State 105"""
    # talk:999001000:"One new message."
    assert t001000000_x46(text1=999001000, z1=91000060)
    """State 87"""
    # talk:931000010:"I see you got a call from V.IV."
    call = t001000000_x33(text3=931000010, z3=91000000)
    if call.Done() and UnkGameCycle() > 1:
        """State 89"""
        # talk:931010010:"Raven."
        assert t001000000_x33(text3=931010010, z3=91000030)
    elif call.Done():
        """State 88"""
        # talk:931001010:"...Raven."
        assert t001000000_x33(text3=931001010, z3=91000030)
    """State 8"""
    # eventflag:3421:	[Garage] Judgment by seeing the story production Chapter 3 progress 2 	【ガレージ】ストーリー演出を見た判定チャプター3進行度2
    SetEventFlag(3421, 1)
    c1_229(7)
    """State 183"""
    c1_230(0)
    return 2
    """State 29"""
    Label('L1')
    # eventflag:3422:	[Garage] Judgment by watching the story production Chapter 3 progress 3 	【ガレージ】ストーリー演出を見た判定チャプター3進行度3, mission:3030:"Attack the Refueling Base"
    if not GetEventFlag(3422) and UnkMissionComplete(3030, 1) == 1:
        """State 28,106"""
        call = t001000000_x15()
        # eventflag:3425:	[Garage] Judgment after seeing the story production Chapter 3 progress 6 	【ガレージ】ストーリー演出を見た判定チャプター3進行度6
        if call.Done() and GetEventFlag(3425) == 1:
            """State 67"""
            # eventflag:3157:	Arena unlock progress 8 	アリーナ解禁進行度8
            if not GetEventFlag(3157):
                """State 117"""
                # talk:999002000:"Two new messages."
                assert t001000000_x46(text1=999002000, z1=91000060)
            else:
                """State 107"""
                Label('L2')
                # talk:999001000:"One new message."
                assert t001000000_x46(text1=999001000, z1=91000060)
        elif call.Done():
            Goto('L2')
        """State 108"""
        # talk:931100010:"Arquebus Group mercenary liaison,\nV.VIII Pater here."
        assert t001000000_x33(text3=931100010, z3=91000070)
        """State 30"""
        # eventflag:3422:	[Garage] Judgment by watching the story production Chapter 3 progress 3 	【ガレージ】ストーリー演出を見た判定チャプター3進行度3
        SetEventFlag(3422, 1)
        c1_229(7)
        """State 38"""
        Label('L3')
        """State 39"""
        Label('L4')
    else:
        """State 31"""
        # eventflag:3423:	[Garage] Judgment by seeing the story production Chapter 3 Progress 4 	【ガレージ】ストーリー演出を見た判定チャプター3進行度4, mission:3420:"Tunnel Sabotage"
        if not GetEventFlag(3423) and UnkMissionComplete(3420, 1) == 1:
            """State 32,109"""
            call = t001000000_x15()
            # eventflag:3425:	[Garage] Judgment after seeing the story production Chapter 3 progress 6 	【ガレージ】ストーリー演出を見た判定チャプター3進行度6
            if call.Done() and GetEventFlag(3425) == 1:
                """State 68"""
                # eventflag:3157:	Arena unlock progress 8 	アリーナ解禁進行度8
                if not GetEventFlag(3157):
                    """State 118"""
                    # talk:999002000:"Two new messages."
                    assert t001000000_x46(text1=999002000, z1=91000060)
                else:
                    """State 110"""
                    Label('L5')
                    # talk:999001000:"One new message."
                    assert t001000000_x46(text1=999001000, z1=91000060)
            elif call.Done():
                Goto('L5')
            """State 111"""
            # talk:931200010:"Attention, G13 Raven!"
            assert t001000000_x33(text3=931200010, z3=91000080)
            """State 33"""
            # eventflag:3423:	[Garage] Judgment by seeing the story production Chapter 3 Progress 4 	【ガレージ】ストーリー演出を見た判定チャプター3進行度4
            SetEventFlag(3423, 1)
            c1_229(7)
            Goto('L3')
        else:
            """State 34"""
            # eventflag:3424:	[Garage] Judgment by watching the story production Chapter 3 progress level 5 	【ガレージ】ストーリー演出を見た判定チャプター3進行度5, mission:2170:"Eliminate V.VII"
            if not GetEventFlag(3424) and UnkMissionComplete(2170, 1) == 1:
                """State 35,112"""
                call = t001000000_x15()
                # eventflag:3425:	[Garage] Judgment after seeing the story production Chapter 3 progress 6 	【ガレージ】ストーリー演出を見た判定チャプター3進行度6
                if call.Done() and GetEventFlag(3425) == 1:
                    """State 69"""
                    # eventflag:3157:	Arena unlock progress 8 	アリーナ解禁進行度8
                    if not GetEventFlag(3157):
                        """State 119"""
                        # talk:999002000:"Two new messages."
                        assert t001000000_x46(text1=999002000, z1=91000060)
                    else:
                        """State 113"""
                        Label('L6')
                        # talk:999001000:"One new message."
                        assert t001000000_x46(text1=999001000, z1=91000060)
                elif call.Done():
                    Goto('L6')
                """State 37"""
                # eventflag:8104:	8104_Event flag for branching in mission_Search in front of wall_Route B (miss) 	8104_ミッション内分岐用イベントフラグ_壁前探索_ルートB（見逃す）
                if GetEventFlag(8104) == 1:
                    """State 114"""
                    # talk:931301010:"Arquebus Group mercenary liaison,\nV.VIII Pater here."
                    assert t001000000_x33(text3=931301010, z3=91000070)
                    """State 74"""
                    UnkUnlockDecal(6606)
                    assert f338() == 1
                else:
                    """State 115"""
                    # talk:931300010:"Raven. You have our gratitude\nfor eliminating Swinburne."
                    assert t001000000_x33(text3=931300010, z3=91000090)
                    """State 76"""
                    UnkUnlockDecal(6603)
                    assert f338() == 1
                """State 36"""
                # eventflag:3424:	[Garage] Judgment by watching the story production Chapter 3 progress level 5 	【ガレージ】ストーリー演出を見た判定チャプター3進行度5
                SetEventFlag(3424, 1)
                c1_229(7)
                Goto('L3')
            else:
                """State 70"""
                # eventflag:3423:	[Garage] Judgment by seeing the story production Chapter 3 Progress 4 	【ガレージ】ストーリー演出を見た判定チャプター3進行度4, mission:7910:"Prevent Corporate Salvage of New Tech"
                if not GetEventFlag(3423) and UnkMissionComplete(7910, 1) == 1:
                    """State 66,169"""
                    call = t001000000_x15()
                    # eventflag:3425:	[Garage] Judgment after seeing the story production Chapter 3 progress 6 	【ガレージ】ストーリー演出を見た判定チャプター3進行度6
                    if call.Done() and GetEventFlag(3425) == 1:
                        """State 72"""
                        # eventflag:3157:	Arena unlock progress 8 	アリーナ解禁進行度8
                        if not GetEventFlag(3157):
                            """State 175"""
                            # talk:931210010:"Raven. I've been thinking about\nwhat Middle Flatwell said."
                            assert t001000000_x33(text3=931210010, z3=91000030)
                            """State 172"""
                            # talk:999001000:"One new message."
                            assert t001000000_x46(text1=999001000, z1=91000060)
                        else:
                            """State 170"""
                            Label('L7')
                            # talk:999000000:"No new messages."
                            assert t001000000_x46(text1=999000000, z1=91000060)
                            """State 176"""
                            # talk:931210010:"Raven. I've been thinking about\nwhat Middle Flatwell said."
                            assert t001000000_x33(text3=931210010, z3=91000030)
                    elif call.Done():
                        Goto('L7')
                    elif call.Done():
                        """State 179"""
                        # talk:999000000:"No new messages."
                        assert t001000000_x46(text1=999000000, z1=91000060)
                        """State 171"""
                        # talk:931210010:"Raven. I've been thinking about\nwhat Middle Flatwell said."
                        assert t001000000_x33(text3=931210010, z3=91000030)
                    """State 71"""
                    # eventflag:3423:	[Garage] Judgment by seeing the story production Chapter 3 Progress 4 	【ガレージ】ストーリー演出を見た判定チャプター3進行度4
                    SetEventFlag(3423, 1)
                    c1_229(7)
                    Goto('L4')
                else:
                    pass
    """State 5"""
    # mission:2170:"Eliminate V.VII", mission:3420:"Tunnel Sabotage", mission:3030:"Attack the Refueling Base", eventflag:3426:	[Garage] Judgment by watching the story production Chapter 3 progress level 7 	【ガレージ】ストーリー演出を見た判定チャプター3進行度7
    if (UnkMissionComplete(2170, 1) == 1 and UnkMissionComplete(3420, 1) == 1 and UnkMissionComplete(3030,
        1) == 1 and not GetEventFlag(3426)):
        """State 6"""
        Label('L8')
        """State 21"""
        # eventflag:3157:	Arena unlock progress 8 	アリーナ解禁進行度8
        if not GetEventFlag(3157) and UnkGameCycle() > 1:
            """State 95"""
            # talk:932010010:"Registration number Rb23, callsign Raven."
            assert t001000000_x33(text3=932010010, z3=91000010)
            """State 94"""
            assert t001000000_x29()
        # eventflag:3153:	Arena unlock progress 4 	アリーナ解禁進行度4
        elif not GetEventFlag(3153):
            """State 116"""
            # talk:932001010:"Registration number Rb23, callsign Raven.\nYour records have been updated."
            assert t001000000_x33(text3=932001010, z3=91000010)
            """State 97"""
            assert t001000000_x10()
        else:
            pass
        """State 19"""
        c1_229(7)
        """State 184"""
        c1_230(0)
        # eventflag:3426:	[Garage] Judgment by watching the story production Chapter 3 progress level 7 	【ガレージ】ストーリー演出を見た判定チャプター3進行度7
        SetEventFlag(3426, 1)
        return 3
    # mission:2170:"Eliminate V.VII", mission:7910:"Prevent Corporate Salvage of New Tech", mission:3030:"Attack the Refueling Base", eventflag:3426:	[Garage] Judgment by watching the story production Chapter 3 progress level 7 	【ガレージ】ストーリー演出を見た判定チャプター3進行度7
    elif (UnkMissionComplete(2170, 1) == 1 and UnkMissionComplete(7910, 1) == 1 and UnkMissionComplete(3030,
          1) == 1 and not GetEventFlag(3426)):
        Goto('L8')
    else:
        """State 40"""
        # eventflag:3427:	[Garage] Judgment by watching the story production Chapter 3 progress level 8 	【ガレージ】ストーリー演出を見た判定チャプター3進行度8, mission:5100:"Survey the Uninhabited Floating City"
        if not GetEventFlag(3427) and UnkMissionComplete(5100, 1) == 1:
            """State 41,120"""
            assert t001000000_x15()
            """State 121"""
            # talk:999000000:"No new messages."
            assert t001000000_x46(text1=999000000, z1=91000060)
            """State 122"""
            # talk:932100010:"...Raven."
            assert t001000000_x33(text3=932100010, z3=91000030)
            """State 24"""
            Label('L9')
            # eventflag:3427:	[Garage] Judgment by watching the story production Chapter 3 progress level 8 	【ガレージ】ストーリー演出を見た判定チャプター3進行度8
            SetEventFlag(3427, 1)
            c1_229(7)
            """State 50"""
            Label('L10')
            """State 51"""
        else:
            """State 22"""
            # mission:5105:"Survey the Uninhabited Floating City", eventflag:3427:	[Garage] Judgment by watching the story production Chapter 3 progress level 8 	【ガレージ】ストーリー演出を見た判定チャプター3進行度8
            if UnkMissionComplete(5105, 1) == 1 and not GetEventFlag(3427):
                """State 23,98"""
                assert t001000000_x15()
                """State 123"""
                # talk:999000000:"No new messages."
                assert t001000000_x46(text1=999000000, z1=91000060)
                """State 99"""
                # talk:932150010:"...Raven."
                assert t001000000_x33(text3=932150010, z3=91000030)
                """State 25"""
                c1_237(13021700)
                assert GetCurrentStateElapsedTime() > 1
                """State 102"""
                # talk:932150020:"...It seems Dolmayan really did\nexperience Contact, like you and I."
                assert t001000000_x33(text3=932150020, z3=91000030)
                Goto('L9')
            else:
                """State 42"""
                # eventflag:3428:	[Garage] Judgment by seeing the story production Chapter 3 progress level 9 	【ガレージ】ストーリー演出を見た判定チャプター3進行度9, mission:7990:"Eliminate the Enforcement Squads"
                if not GetEventFlag(3428) and UnkMissionComplete(7990, 1) == 1:
                    """State 43,124"""
                    assert t001000000_x15()
                    """State 125"""
                    # talk:999001000:"One new message."
                    assert t001000000_x46(text1=999001000, z1=91000060)
                    """State 126"""
                    # talk:932170010:"G13 Raven!\nThat was a beautiful massacre at the Wall."
                    assert t001000000_x33(text3=932170010, z3=91000080)
                else:
                    """State 45"""
                    # eventflag:3428:	[Garage] Judgment by seeing the story production Chapter 3 progress level 9 	【ガレージ】ストーリー演出を見た判定チャプター3進行度9, mission:3430:"Destroy the Special Forces Craft"
                    if not GetEventFlag(3428) and UnkMissionComplete(3430, 1) == 1:
                        """State 46,127"""
                        assert t001000000_x15()
                        """State 128"""
                        # talk:999001000:"One new message."
                        assert t001000000_x46(text1=999001000, z1=91000060)
                        """State 129"""
                        # talk:932180010:"Raven.\nThank you for taking the CATAPHRACT mission."
                        assert t001000000_x33(text3=932180010, z3=91000090)
                    else:
                        """State 47"""
                        # eventflag:3429:	[Garage] Judgment by watching the story production Chapter 3 progress 10 	【ガレージ】ストーリー演出を見た判定チャプター3進行度10, mission:2220:"Heavy Missile Launch Support"
                        if not GetEventFlag(3429) and UnkMissionComplete(2220, 1) == 1:
                            """State 48,130"""
                            assert t001000000_x15()
                            """State 131"""
                            # talk:999001000:"One new message."
                            assert t001000000_x46(text1=999001000, z1=91000060)
                            """State 132"""
                            # talk:932200010:""Chatty" Stick, RaD.\nThanks for helping with the firework show."
                            assert t001000000_x33(text3=932200010, z3=91000100)
                            """State 49"""
                            # eventflag:3429:	[Garage] Judgment by watching the story production Chapter 3 progress 10 	【ガレージ】ストーリー演出を見た判定チャプター3進行度10
                            SetEventFlag(3429, 1)
                            c1_229(7)
                            Goto('L10')
                        else:
                            Goto('L11')
                """State 44"""
                # eventflag:3428:	[Garage] Judgment by seeing the story production Chapter 3 progress level 9 	【ガレージ】ストーリー演出を見た判定チャプター3進行度9
                SetEventFlag(3428, 1)
                c1_229(7)
                Goto('L10')
        """State 9"""
        Label('L11')
        # eventflag:3460:	[Garage] Judgment by watching the story production Chapter 3 progress level 11 	【ガレージ】ストーリー演出を見た判定チャプター3進行度11, mission:5100:"Survey the Uninhabited Floating City", mission:3430:"Destroy the Special Forces Craft", mission:2220:"Heavy Missile Launch Support"
        if (not GetEventFlag(3460) and UnkMissionComplete(5100, 1) == 1 and UnkMissionComplete(3430,
            1) == 1 and UnkMissionComplete(2220, 1) == 1):
            """State 10"""
            Label('L12')
            # eventflag:6000:	A route clear 	Aルートクリア, eventflag:6001:	B route clear 	Bルートクリア
            if GetEventFlag(6000) == 1 and GetEventFlag(6001) == 1:
                """State 20"""
                # eventflag:6016:	Arena unlocking progress 7 take over 	アリーナ解禁進行度7　引継ぎ
                if not GetEventFlag(6016):
                    """State 96"""
                    # talk:933020010:"Raven, just so you know..."
                    assert t001000000_x33(text3=933020010, z3=91000030)
                    """State 101"""
                    assert t001000000_x43()
                else:
                    pass
            else:
                """State 79"""
                if GetEventFlag(6245) == 1:
                    pass
                else:
                    """State 180"""
                    assert t001000000_x50()
            """State 11"""
            # eventflag:3460:	[Garage] Judgment by watching the story production Chapter 3 progress level 11 	【ガレージ】ストーリー演出を見た判定チャプター3進行度11
            SetEventFlag(3460, 1)
            c1_229(7)
            """State 185"""
            c1_230(0)
            return 4
        # eventflag:3460:	[Garage] Judgment by watching the story production Chapter 3 progress level 11 	【ガレージ】ストーリー演出を見た判定チャプター3進行度11, mission:5105:"Survey the Uninhabited Floating City", mission:2220:"Heavy Missile Launch Support", mission:3430:"Destroy the Special Forces Craft"
        elif (not GetEventFlag(3460) and UnkMissionComplete(5105, 1) == 1 and UnkMissionComplete(2220,
              1) == 1 and UnkMissionComplete(3430, 1) == 1):
            Goto('L12')
        # eventflag:3460:	[Garage] Judgment by watching the story production Chapter 3 progress level 11 	【ガレージ】ストーリー演出を見た判定チャプター3進行度11, mission:5100:"Survey the Uninhabited Floating City", mission:2220:"Heavy Missile Launch Support", mission:7990:"Eliminate the Enforcement Squads"
        elif (not GetEventFlag(3460) and UnkMissionComplete(5100, 1) == 1 and UnkMissionComplete(2220,
              1) == 1 and UnkMissionComplete(7990, 1) == 1):
            Goto('L12')
        # eventflag:3460:	[Garage] Judgment by watching the story production Chapter 3 progress level 11 	【ガレージ】ストーリー演出を見た判定チャプター3進行度11, mission:5105:"Survey the Uninhabited Floating City", mission:2220:"Heavy Missile Launch Support", mission:7990:"Eliminate the Enforcement Squads"
        elif (not GetEventFlag(3460) and UnkMissionComplete(5105, 1) == 1 and UnkMissionComplete(2220,
              1) == 1 and UnkMissionComplete(7990, 1) == 1):
            Goto('L12')
        else:
            """State 16"""
            # eventflag:3461:	[Garage] Judgment by watching the story production Chapter 3 progress level 12 	【ガレージ】ストーリー演出を見た判定チャプター3進行度12, mission:3043:"Attack the Old Spaceport"
            if not GetEventFlag(3461) and UnkMissionComplete(3043, 1) == 1:
                """State 134"""
                call = t001000000_x15()
                # mission:2250:"Escort the Weaponized Mining Ship"
                if call.Done() and UnkMissionComplete(2250, 1) == 1:
                    """State 90"""
                    # talk:934020010:"Raven."
                    assert t001000000_x33(text3=934020010, z3=91000030)
                elif call.Done():
                    pass
                """State 52"""
                if UnkGameCycle() > 1:
                    """State 138"""
                    # talk:999002000:"Two new messages."
                    assert t001000000_x46(text1=999002000, z1=91000060)
                    """State 139"""
                    # talk:934001010:"Heard the news, tourist."
                    call = t001000000_x33(text3=934001010, z3=91000040)
                    # mission:7910:"Prevent Corporate Salvage of New Tech"
                    if call.Done() and UnkMissionComplete(7910, 1) == 1:
                        """State 141"""
                        # talk:934010010:"Sorry to impose on you, Raven,\nbut I've just sent you an urgent request."
                        assert t001000000_x33(text3=934010010, z3=91000090)
                    elif call.Done():
                        """State 140"""
                        # talk:934002010:"This is V.VIII Pater. Your performance in\nthe spaceport raid was admirable."
                        assert t001000000_x33(text3=934002010, z3=91000070)
                # mission:3043:"Attack the Old Spaceport", eventflag:3153:	Arena unlock progress 4 	アリーナ解禁進行度4
                elif UnkMissionComplete(3043, 1) == 1 and not GetEventFlag(3153):
                    """State 133"""
                    # talk:999003000:"Three new messages."
                    assert t001000000_x46(text1=999003000, z1=91000060)
                    """State 136"""
                    # talk:934001010:"Heard the news, tourist."
                    assert t001000000_x33(text3=934001010, z3=91000040)
                    """State 137"""
                    # talk:934002010:"This is V.VIII Pater. Your performance in\nthe spaceport raid was admirable."
                    assert t001000000_x33(text3=934002010, z3=91000070)
                    """State 135"""
                    # talk:934000010:"Registration number Rb23, callsign Raven.\nYour records have been updated."
                    assert t001000000_x33(text3=934000010, z3=91000010)
                    """State 92"""
                    assert t001000000_x10()
                """State 18"""
                # eventflag:3461:	[Garage] Judgment by watching the story production Chapter 3 progress level 12 	【ガレージ】ストーリー演出を見た判定チャプター3進行度12
                SetEventFlag(3461, 1)
                c1_229(7)
                """State 186"""
                c1_230(0)
                return 5
            else:
                """State 26"""
                # eventflag:3462:	[Garage] Judgment by seeing the story production Chapter 3 progress level 13 	【ガレージ】ストーリー演出を見た判定チャプター3進行度13, mission:3320:"Eliminate "Honest" Brute"
                if not GetEventFlag(3462) and UnkMissionComplete(3320, 1) == 1:
                    """State 53,142"""
                    call = t001000000_x15()
                    # eventflag:3465:	[Garage] Judgment after seeing the story production Chapter 3 progress 16 	【ガレージ】ストーリー演出を見た判定チャプター3進行度16
                    if call.Done() and GetEventFlag(3465) == 1:
                        """State 156"""
                        # talk:999002000:"Two new messages."
                        assert t001000000_x46(text1=999002000, z1=91000060)
                        """State 157"""
                        # talk:934100010:"This is "Chatty" Stick, RaD."
                        assert t001000000_x33(text3=934100010, z3=91000100)
                        """State 77"""
                        UnkUnlockDecal(6604)
                        assert f338() == 1
                        """State 158"""
                        # talk:935100010:"...Time for work, 621."
                        assert t001000000_x33(text3=935100010, z3=91000000)
                    elif call.Done():
                        """State 143"""
                        # talk:999001000:"One new message."
                        assert t001000000_x46(text1=999001000, z1=91000060)
                        """State 144"""
                        # talk:934100010:"This is "Chatty" Stick, RaD."
                        assert t001000000_x33(text3=934100010, z3=91000100)
                        """State 73"""
                        UnkUnlockDecal(6604)
                        assert f338() == 1
                    """State 27"""
                    # eventflag:3462:	[Garage] Judgment by seeing the story production Chapter 3 progress level 13 	【ガレージ】ストーリー演出を見た判定チャプター3進行度13
                    SetEventFlag(3462, 1)
                    c1_229(7)
                    """State 64"""
                    Label('L13')
                    """State 65"""
                else:
                    """State 56"""
                    # eventflag:3463:	[Garage] Judgment by seeing the story production Chapter 3 progress level 14 	【ガレージ】ストーリー演出を見た判定チャプター3進行度14, mission:7950:"Defend the Old Spaceport"
                    if not GetEventFlag(3463) and UnkMissionComplete(7950, 1) == 1:
                        """State 54,145"""
                        call = t001000000_x15()
                        # eventflag:3465:	[Garage] Judgment after seeing the story production Chapter 3 progress 16 	【ガレージ】ストーリー演出を見た判定チャプター3進行度16
                        if call.Done() and GetEventFlag(3465) == 1:
                            """State 160"""
                            # talk:934250010:"I've looked into the other "Raven"...\nthe independent mercenary who attacked you."
                            assert t001000000_x33(text3=934250010, z3=91000030)
                            """State 78"""
                            UnkUnlockDecal(6610)
                            assert f338() == 1
                            """State 159"""
                            # talk:999001000:"One new message."
                            assert t001000000_x46(text1=999001000, z1=91000060)
                            """State 161"""
                            # talk:935100010:"...Time for work, 621."
                            assert t001000000_x33(text3=935100010, z3=91000000)
                        elif call.Done():
                            """State 146"""
                            # talk:999000000:"No new messages."
                            assert t001000000_x46(text1=999000000, z1=91000060)
                            """State 91"""
                            # talk:934250010:"I've looked into the other "Raven"...\nthe independent mercenary who attacked you."
                            assert t001000000_x33(text3=934250010, z3=91000030)
                            """State 75"""
                            UnkUnlockDecal(6610)
                            assert f338() == 1
                    else:
                        """State 58"""
                        # eventflag:3463:	[Garage] Judgment by seeing the story production Chapter 3 progress level 14 	【ガレージ】ストーリー演出を見た判定チャプター3進行度14, mission:2240:"Defend the Dam Complex"
                        if not GetEventFlag(3463) and UnkMissionComplete(2240, 1) == 1:
                            """State 57,148"""
                            call = t001000000_x15()
                            # eventflag:3465:	[Garage] Judgment after seeing the story production Chapter 3 progress 16 	【ガレージ】ストーリー演出を見た判定チャプター3進行度16
                            if call.Done() and GetEventFlag(3465) == 1:
                                """State 162"""
                                # talk:934260010:"I've looked into "Branch"...\nthe independent mercenaries who attacked you."
                                assert t001000000_x33(text3=934260010, z3=91000030)
                                """State 164"""
                                # talk:999001000:"One new message."
                                assert t001000000_x46(text1=999001000, z1=91000060)
                                """State 163"""
                                # talk:935100010:"...Time for work, 621."
                                assert t001000000_x33(text3=935100010, z3=91000000)
                            elif call.Done():
                                """State 149"""
                                # talk:999000000:"No new messages."
                                assert t001000000_x46(text1=999000000, z1=91000060)
                                """State 147"""
                                # talk:934260010:"I've looked into "Branch"...\nthe independent mercenaries who attacked you."
                                assert t001000000_x33(text3=934260010, z3=91000030)
                        else:
                            """State 60"""
                            # eventflag:3464:	[Garage] Judgment by seeing the story production Chapter 3 progress level 15 	【ガレージ】ストーリー演出を見た判定チャプター3進行度15, mission:3500:"Historic Data Recovery"
                            if not GetEventFlag(3464) and UnkMissionComplete(3500, 1) == 1:
                                """State 59,151"""
                                assert t001000000_x15()
                                """State 152"""
                                # talk:999001000:"One new message."
                                call = t001000000_x46(text1=999001000, z1=91000060)
                                # eventflag:3465:	[Garage] Judgment after seeing the story production Chapter 3 progress 16 	【ガレージ】ストーリー演出を見た判定チャプター3進行度16
                                if call.Done() and GetEventFlag(3465) == 1:
                                    """State 165"""
                                    # talk:934351010:"...What kept you, 621?"
                                    assert t001000000_x33(text3=934351010, z3=91000000)
                                elif call.Done():
                                    """State 150"""
                                    # talk:934350010:"...What kept you, 621?"
                                    assert t001000000_x33(text3=934350010, z3=91000000)
                            else:
                                """State 62"""
                                # eventflag:3464:	[Garage] Judgment by seeing the story production Chapter 3 progress level 15 	【ガレージ】ストーリー演出を見た判定チャプター3進行度15, mission:2211:"Coral Export Denial"
                                if not GetEventFlag(3464) and UnkMissionComplete(2211, 1) == 1:
                                    """State 63,154"""
                                    call = t001000000_x15()
                                    # eventflag:3465:	[Garage] Judgment after seeing the story production Chapter 3 progress 16 	【ガレージ】ストーリー演出を見た判定チャプター3進行度16
                                    if call.Done() and GetEventFlag(3465) == 1:
                                        """State 173"""
                                        # talk:934370010:"Raven, there's something that\ntroubles me about ALLMIND."
                                        assert t001000000_x33(text3=934370010, z3=91000030)
                                        """State 166"""
                                        # talk:999001000:"One new message."
                                        assert t001000000_x46(text1=999001000, z1=91000060)
                                        """State 174"""
                                        # talk:935100010:"...Time for work, 621."
                                        assert t001000000_x33(text3=935100010, z3=91000000)
                                    elif call.Done():
                                        """State 155"""
                                        # talk:999000000:"No new messages."
                                        assert t001000000_x46(text1=999000000, z1=91000060)
                                        """State 153"""
                                        # talk:934370010:"Raven, there's something that\ntroubles me about ALLMIND."
                                        assert t001000000_x33(text3=934370010, z3=91000030)
                                else:
                                    Goto('L14')
                            """State 61"""
                            # eventflag:3464:	[Garage] Judgment by seeing the story production Chapter 3 progress level 15 	【ガレージ】ストーリー演出を見た判定チャプター3進行度15
                            SetEventFlag(3464, 1)
                            c1_229(7)
                            Goto('L13')
                    """State 55"""
                    # eventflag:3463:	[Garage] Judgment by seeing the story production Chapter 3 progress level 14 	【ガレージ】ストーリー演出を見た判定チャプター3進行度14
                    SetEventFlag(3463, 1)
                    c1_229(7)
                    Goto('L13')
                """State 12"""
                Label('L14')
                # eventflag:3466:	[Garage] Judgment by seeing the story production Chapter 3 progress level 17 	【ガレージ】ストーリー演出を見た判定チャプター3進行度17, mission:3320:"Eliminate "Honest" Brute", mission:7950:"Defend the Old Spaceport", mission:3500:"Historic Data Recovery"
                if (not GetEventFlag(3466) and UnkMissionComplete(3320, 1) == 1 and UnkMissionComplete(7950,
                    1) == 1 and UnkMissionComplete(3500, 1) == 1):
                    """State 13"""
                    Label('L15')
                    if UnkGameCycle() > 1:
                        pass
                    else:
                        """State 177"""
                        assert (t001000000_x48() and (not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1
                                and not CheckSpecificPersonGenericDialogIsOpen(0)) and GetCurrentStateElapsedFrames()
                                > 1))
                        """State 15"""
                        # weapon:30270000:VE-60SNA
                        GiveItemDirectly(0, 30270000, 1)
                    """State 14"""
                    # eventflag:3466:	[Garage] Judgment by seeing the story production Chapter 3 progress level 17 	【ガレージ】ストーリー演出を見た判定チャプター3進行度17
                    SetEventFlag(3466, 1)
                    UnkUnlockDecal(6609)
                    """State 187"""
                    return 6
                # eventflag:3466:	[Garage] Judgment by seeing the story production Chapter 3 progress level 17 	【ガレージ】ストーリー演出を見た判定チャプター3進行度17, mission:2211:"Coral Export Denial", mission:2240:"Defend the Dam Complex", mission:3320:"Eliminate "Honest" Brute"
                elif (not GetEventFlag(3466) and UnkMissionComplete(2211, 1) == 1 and UnkMissionComplete(2240,
                      1) == 1 and UnkMissionComplete(3320, 1) == 1):
                    Goto('L15')
                # eventflag:3466:	[Garage] Judgment by seeing the story production Chapter 3 progress level 17 	【ガレージ】ストーリー演出を見た判定チャプター3進行度17, mission:3320:"Eliminate "Honest" Brute", mission:2240:"Defend the Dam Complex", mission:3500:"Historic Data Recovery"
                elif (not GetEventFlag(3466) and UnkMissionComplete(3320, 1) == 1 and UnkMissionComplete(2240,
                      1) == 1 and UnkMissionComplete(3500, 1) == 1):
                    Goto('L15')
                # eventflag:3466:	[Garage] Judgment by seeing the story production Chapter 3 progress level 17 	【ガレージ】ストーリー演出を見た判定チャプター3進行度17, mission:2211:"Coral Export Denial", mission:7950:"Defend the Old Spaceport", mission:3320:"Eliminate "Honest" Brute"
                elif (not GetEventFlag(3466) and UnkMissionComplete(2211, 1) == 1 and UnkMissionComplete(7950,
                      1) == 1 and UnkMissionComplete(3320, 1) == 1):
                    Goto('L15')
                # mission:3320:"Eliminate "Honest" Brute", mission:7950:"Defend the Old Spaceport", mission:3500:"Historic Data Recovery", eventflag:3466:	[Garage] Judgment by seeing the story production Chapter 3 progress level 17 	【ガレージ】ストーリー演出を見た判定チャプター3進行度17
                elif (UnkMissionComplete(3320, 1) == 1 and UnkMissionComplete(7950, 1) == 1 and UnkMissionComplete(3500,
                      1) == 1 and not GetEventFlag(3466)):
                    Goto('L15')
                else:
                    """State 181"""
                    return 0

def t001000000_x12():
    """State 0,1"""
    c1_224(50030)
    # eventflag:3430:	[Garage] Judgment by seeing the story production_Chapter 4 progress 1 	【ガレージ】ストーリー演出を見た判定_チャプター4進行度1
    if not GetEventFlag(3430):
        pass
    else:
        Goto('L1')
    """State 2,31"""
    call = t001000000_x15()
    # mission:2211:"Coral Export Denial"
    if call.Done() and UnkMissionComplete(2211, 1) == 1:
        """State 55"""
        # talk:999008000:"Augmented human C4-621: Entering Standard Mode."
        assert t001000000_x46(text1=999008000, z1=91000060)
        """State 71"""
        # talk:940000010:"Doing okay, 621?"
        assert t001000000_x33(text3=940000010, z3=91000000)
        """State 52"""
        # talk:940020010:"...Raven."
        assert t001000000_x33(text3=940020010, z3=91000030)
    elif call.Done() and UnkGameCycle() > 2:
        """State 76"""
        # talk:999008000:"Augmented human C4-621: Entering Standard Mode."
        assert t001000000_x46(text1=999008000, z1=91000060)
        """State 37"""
        Label('L0')
        # talk:940000010:"Doing okay, 621?"
        assert t001000000_x33(text3=940000010, z3=91000000)
        """State 44"""
        # talk:940001010:"..."
        call = t001000000_x33(text3=940001010, z3=91000030)
        # eventflag:3158:	Arena unlock progress 9 	アリーナ解禁進行度9
        if call.Done() and (UnkGameCycle() > 1 and not GetEventFlag(3158)):
            """State 38"""
            # talk:940010010:"Registration number Rb23, callsign Raven."
            assert t001000000_x33(text3=940010010, z3=91000010)
            """State 42"""
            assert t001000000_x35()
            """State 36"""
            assert t001000000_x25()
        # eventflag:3158:	Arena unlock progress 9 	アリーナ解禁進行度9
        elif call.Done() and GetEventFlag(3158) == 1:
            pass
        elif call.Done():
            """State 39"""
            # talk:940002010:"Registration number Rb23, callsign Raven.\nYour records have been updated."
            assert t001000000_x33(text3=940002010, z3=91000010)
            """State 32"""
            assert t001000000_x10()
            """State 35"""
            assert t001000000_x22() and f320(7) == 1
    elif call.Done():
        """State 56"""
        # talk:999009000:"Augmented human C4-621: Entering Standard Mode."
        assert t001000000_x46(text1=999009000, z1=91000060)
        Goto('L0')
    """State 3"""
    c1_229(7)
    # eventflag:3430:	[Garage] Judgment by seeing the story production_Chapter 4 progress 1 	【ガレージ】ストーリー演出を見た判定_チャプター4進行度1
    SetEventFlag(3430, 1)
    """State 78"""
    c1_230(0)
    return 1
    """State 16"""
    Label('L1')
    # mission:4000:"Underground Exploration – Depth 1", eventflag:3431:	[Garage] Judgment by seeing the story production_Chapter 4 progress 2 	【ガレージ】ストーリー演出を見た判定_チャプター4進行度2
    if UnkMissionComplete(4000, 1) == 1 and not GetEventFlag(3431):
        pass
    else:
        Goto('L2')
    """State 17,57"""
    assert t001000000_x15()
    """State 58"""
    # talk:999000000:"No new messages."
    assert t001000000_x46(text1=999000000, z1=91000060)
    """State 18"""
    c1_229(7)
    # eventflag:3431:	[Garage] Judgment by seeing the story production_Chapter 4 progress 2 	【ガレージ】ストーリー演出を見た判定_チャプター4進行度2
    SetEventFlag(3431, 1)
    """State 82"""
    return 5
    """State 19"""
    Label('L2')
    # mission:4010:"Underground Exploration – Depth 2", eventflag:3432:	[Garage] Judgment by seeing the story production_Chapter 4 progress 3 	【ガレージ】ストーリー演出を見た判定_チャプター4進行度3
    if UnkMissionComplete(4010, 1) == 1 and not GetEventFlag(3432):
        pass
    # mission:4015:"Underground Exploration – Depth 2", eventflag:3432:	[Garage] Judgment by seeing the story production_Chapter 4 progress 3 	【ガレージ】ストーリー演出を見た判定_チャプター4進行度3
    elif UnkMissionComplete(4015, 1) == 1 and not GetEventFlag(3432):
        pass
    else:
        Goto('L3')
    """State 20,59"""
    call = t001000000_x15()
    # eventflag:6520:	Obtain parts by clearing the rail 	レイルクリアでパーツ入手, mission:4010:"Underground Exploration – Depth 2"
    if call.Done() and (not GetEventFlag(6520) and UnkMissionComplete(4010, 1) == 1):
        """State 30"""
        # protector:50000300:HD-012 MELANDER C3
        GiveItemDirectly(1, 50000300, 1)
        # protector:51000300:BD-012 MELANDER C3
        GiveItemDirectly(1, 51000300, 1)
        # protector:52000300:AR-012 MELANDER C3
        GiveItemDirectly(1, 52000300, 1)
        # protector:53000300:LG-012 MELANDER C3
        GiveItemDirectly(1, 53000300, 1)
        # eventflag:6520:	Obtain parts by clearing the rail 	レイルクリアでパーツ入手
        SetEventFlag(6520, 1)
        assert f338() == 1
    elif call.Done():
        pass
    """State 60"""
    # talk:999000000:"No new messages."
    call = t001000000_x46(text1=999000000, z1=91000060)
    # eventflag:6000:	A route clear 	Aルートクリア, eventflag:6001:	B route clear 	Bルートクリア
    if call.Done() and (GetEventFlag(6000) == 1 and GetEventFlag(6001) == 1):
        """State 9"""
        # eventflag:6000:	A route clear 	Aルートクリア, eventflag:6001:	B route clear 	Bルートクリア
        assert GetEventFlag(6000) == 1 and GetEventFlag(6001) == 1
        """State 10"""
        # eventflag:6017:	Arena unlocking progress level 8 takeover 	アリーナ解禁進行度8　引継ぎ
        if not GetEventFlag(6017):
            """State 43"""
            # talk:940021010:"Registration number Rb23, callsign Raven.\nYour records have been updated."
            assert t001000000_x33(text3=940021010, z3=91000030)
            """State 53"""
            assert t001000000_x44()
        else:
            pass
    elif call.Done():
        pass
    """State 21"""
    c1_229(7)
    # eventflag:3432:	[Garage] Judgment by seeing the story production_Chapter 4 progress 3 	【ガレージ】ストーリー演出を見た判定_チャプター4進行度3
    SetEventFlag(3432, 1)
    """State 83"""
    return 6
    """State 4"""
    Label('L3')
    # eventflag:3433:	[Garage] Judgment by seeing the story production_Chapter 4 progress 4 	【ガレージ】ストーリー演出を見た判定_チャプター4進行度4, mission:4020:"Underground Exploration – Depth 3"
    if not GetEventFlag(3433) and UnkMissionComplete(4020, 1) == 1:
        pass
    else:
        Goto('L4')
    """State 5,33"""
    call = t001000000_x15()
    # mission:2211:"Coral Export Denial"
    if call.Done() and UnkMissionComplete(2211, 1) == 1:
        """State 72"""
        # talk:999000000:"No new messages."
        assert t001000000_x46(text1=999000000, z1=91000060)
        """State 54"""
        # talk:943020010:"Raven."
        assert t001000000_x33(text3=943020010, z3=91000030)
    elif call.Done() and UnkGameCycle() > 1:
        """State 62"""
        # talk:999000000:"No new messages."
        assert t001000000_x46(text1=999000000, z1=91000060)
        """State 74"""
        # talk:943010010:"Raven."
        assert t001000000_x33(text3=943010010, z3=91000030)
    elif call.Done():
        """State 73"""
        # talk:943010010:"Raven."
        assert t001000000_x33(text3=943010010, z3=91000030)
        """State 61"""
        # talk:999001000:"One new message."
        assert t001000000_x46(text1=999001000, z1=91000060)
        """State 45"""
        # talk:943001010:"Registration number Rb23, callsign Raven.\nYour records have been updated."
        assert t001000000_x33(text3=943001010, z3=91000010)
        """State 41"""
        assert t001000000_x10()
    """State 6"""
    c1_229(7)
    # eventflag:3433:	[Garage] Judgment by seeing the story production_Chapter 4 progress 4 	【ガレージ】ストーリー演出を見た判定_チャプター4進行度4
    SetEventFlag(3433, 1)
    """State 79"""
    c1_230(0)
    return 2
    """State 11"""
    Label('L4')
    # mission:7930:"Intercept the Redguns", eventflag:3434:	[Garage] Judgment by seeing the story production_Chapter 4 progress 5 	【ガレージ】ストーリー演出を見た判定_チャプター4進行度5
    if UnkMissionComplete(7930, 1) == 1 and not GetEventFlag(3434):
        """State 12,46"""
        assert t001000000_x15()
        """State 65"""
        # talk:999001000:"One new message."
        assert t001000000_x46(text1=999001000, z1=91000060)
        """State 47"""
        # talk:943150010:"Didn't think I'd see the end of the Redguns..."
        assert t001000000_x33(text3=943150010, z3=91000000)
        """State 50"""
        # talk:943150070:"..."
        assert t001000000_x33(text3=943150070, z3=91000030)
        """State 29"""
        UnkUnlockDecal(6608)
    else:
        """State 22"""
        # eventflag:3434:	[Garage] Judgment by seeing the story production_Chapter 4 progress 5 	【ガレージ】ストーリー演出を見た判定_チャプター4進行度5, mission:4110:"Ambush the Vespers"
        if not GetEventFlag(3434) and UnkMissionComplete(4110, 1) == 1:
            """State 13,66"""
            assert t001000000_x15()
            """State 67"""
            # talk:999001000:"One new message."
            assert t001000000_x46(text1=999001000, z1=91000060)
            """State 48"""
            # talk:943160010:"About the request to attack the Redguns...\nSounds like V.IV Rusty took care of it."
            assert t001000000_x33(text3=943160010, z3=91000000)
            """State 75"""
            # talk:943150070:"..."
            assert t001000000_x33(text3=943150070, z3=91000030)
        else:
            """State 23"""
            # eventflag:3434:	[Garage] Judgment by seeing the story production_Chapter 4 progress 5 	【ガレージ】ストーリー演出を見た判定_チャプター4進行度5, mission:7940:"Eliminate V.III"
            if not GetEventFlag(3434) and UnkMissionComplete(7940, 1) == 1:
                """State 14,63"""
                # talk:999001000:"One new message."
                assert t001000000_x46(text1=999001000, z1=91000060)
                """State 49"""
                # talk:943170010:"Augmented human C4-621—Raven."
                assert t001000000_x33(text3=943170010, z3=91000010)
                """State 28"""
                UnkUnlockDecal(6602)
            else:
                """State 7"""
                # eventflag:3435:	[Garage] Judgment by seeing the story production_Chapter 4 progress 6 	【ガレージ】ストーリー演出を見た判定_チャプター4進行度6, mission:4021:"Unknown Territory Survey"
                if not GetEventFlag(3435) and UnkMissionComplete(4021, 1) == 1:
                    """State 8"""
                    Label('L5')
                    """State 34"""
                    assert t001000000_x15()
                    """State 40"""
                    # talk:945000010:"Raven."
                    assert t001000000_x33(text3=945000010, z3=91000030)
                    """State 68"""
                    # talk:999006000:"Incoming comms."
                    assert t001000000_x46(text1=999006000, z1=91000060)
                    """State 51"""
                    # talk:945001010:"Let me tell you a story before you go."
                    assert t001000000_x33(text3=945001010, z3=91000000)
                    """State 15"""
                    c1_229(7)
                    # eventflag:3435:	[Garage] Judgment by seeing the story production_Chapter 4 progress 6 	【ガレージ】ストーリー演出を見た判定_チャプター4進行度6
                    SetEventFlag(3435, 1)
                    UnkUnlockDecal(6601)
                # eventflag:3435:	[Garage] Judgment by seeing the story production_Chapter 4 progress 6 	【ガレージ】ストーリー演出を見た判定_チャプター4進行度6, mission:4026:"Unknown Territory Survey"
                elif not GetEventFlag(3435) and UnkMissionComplete(4026, 1) == 1:
                    Goto('L5')
                else:
                    """State 25"""
                    # eventflag:3436:	[Garage] Judgment by seeing the story production_Chapter 4 progress level 7 	【ガレージ】ストーリー演出を見た判定_チャプター4進行度7, mission:4035:"Reach the Coral Convergence"
                    if not GetEventFlag(3436) and UnkMissionComplete(4035, 1) == 1:
                        """State 26,69"""
                        assert t001000000_x15()
                        """State 64"""
                        # talk:999000000:"No new messages."
                        assert t001000000_x46(text1=999000000, z1=91000060)
                        """State 70"""
                        # talk:980000010:"We've received a message from ALLMIND."
                        assert t001000000_x33(text3=980000010, z3=91000030)
                        """State 27"""
                        c1_229(7)
                        # eventflag:3436:	[Garage] Judgment by seeing the story production_Chapter 4 progress level 7 	【ガレージ】ストーリー演出を見た判定_チャプター4進行度7
                        SetEventFlag(3436, 1)
                    else:
                        """State 77"""
                        return 0
                """State 80"""
                c1_230(0)
                return 3
    """State 24"""
    c1_229(7)
    # eventflag:3434:	[Garage] Judgment by seeing the story production_Chapter 4 progress 5 	【ガレージ】ストーリー演出を見た判定_チャプター4進行度5
    SetEventFlag(3434, 1)
    """State 81"""
    c1_230(0)
    return 4

def t001000000_x13():
    """State 0"""
    # mission:5110:"Regain Control of the Xylem"
    if UnkMissionComplete(5110, 1) == 1:
        """State 19"""
        Label('L0')
        c1_224(43000)
    # mission:5030:"Destroy the Drive Block"
    elif UnkMissionComplete(5030, 1) == 1:
        Goto('L0')
    # mission:5040:"Breach the Kármán Line"
    elif UnkMissionComplete(5040, 1) == 1:
        Goto('L0')
    else:
        """State 20"""
        c1_224(40020)
    """State 1"""
    # eventflag:3440:	[Garage] Judgment by seeing the story production_Chapter 5 progress 1 	【ガレージ】ストーリー演出を見た判定_チャプター5進行度1, mission:4200:"Escape"
    if not GetEventFlag(3440) and UnkMissionComplete(4200, 1) == 1:
        """State 14,34"""
        call = t001000000_x15()
        # eventflag:6522:	Get parts by clearing jailbreak 	脱獄クリアでパーツ入手, mission:4200:"Escape"
        if call.Done() and (not GetEventFlag(6522) and UnkMissionComplete(4200, 1) == 1):
            """State 25"""
            # protector:50900000:AH-J-124/RC JAILBREAK
            GiveItemDirectly(1, 50900000, 1)
            # protector:51900000:AC-J-120/RC JAILBREAK
            GiveItemDirectly(1, 51900000, 1)
            # protector:52900000:AA-J-123/RC JAILBREAK
            GiveItemDirectly(1, 52900000, 1)
            # protector:53900000:AL-J-121/RC JAILBREAK
            GiveItemDirectly(1, 53900000, 1)
            # eventflag:6522:	Get parts by clearing jailbreak 	脱獄クリアでパーツ入手
            SetEventFlag(6522, 1)
            assert f338() == 1
        elif call.Done():
            pass
        """State 36"""
        # talk:999004000:"Augmented human C4-621: Entering Standard Mode."
        assert t001000000_x46(text1=999004000, z1=91000060)
        """State 35"""
        # talk:950100010:"Back in your old AC?\nYou were made for each other."
        call = t001000000_x33(text3=950100010, z3=91000040)
        # eventflag:6260:	prison break 	脱獄
        if call.Done() and (UnkGameCycle() > 0 and not GetEventFlag(6260)):
            """State 26"""
            call = t001000000_x23()
            if call.Done():
                pass
            elif call.Done():
                pass
        elif call.Done():
            pass
        """State 15"""
        # eventflag:3440:	[Garage] Judgment by seeing the story production_Chapter 5 progress 1 	【ガレージ】ストーリー演出を見た判定_チャプター5進行度1
        SetEventFlag(3440, 1)
        """State 47"""
        c1_230(0)
        return 1
    else:
        """State 8"""
        # eventflag:3440:	[Garage] Judgment by seeing the story production_Chapter 5 progress 1 	【ガレージ】ストーリー演出を見た判定_チャプター5進行度1, mission:4100:"MIA"
        if not GetEventFlag(3440) and UnkMissionComplete(4100, 1) == 1:
            """State 9,31"""
            assert t001000000_x15()
            """State 37"""
            # talk:999007000:"Augmented human C4-621: Entering Standard Mode."
            assert t001000000_x46(text1=999007000, z1=91000060)
            """State 32"""
            # talk:981100010:"Raven, we've received a request from ALLMIND."
            assert t001000000_x33(text3=981100010, z3=91000030)
            """State 10"""
            # eventflag:3440:	[Garage] Judgment by seeing the story production_Chapter 5 progress 1 	【ガレージ】ストーリー演出を見た判定_チャプター5進行度1
            SetEventFlag(3440, 1)
            # eventflag:3447:	[Garage] Current Route C 	【ガレージ】現在Cルート
            SetEventFlag(3447, 1)
            """State 50"""
            c1_230(0)
            return 4
        else:
            """State 16"""
            # eventflag:3441:	[Garage] Judgment by seeing the story production_Chapter 5 progress 2 	【ガレージ】ストーリー演出を見た判定_チャプター5進行度2, mission:5010:"Take the Uninhabited Floating City"
            if not GetEventFlag(3441) and UnkMissionComplete(5010, 1) == 1:
                """State 17,38"""
                assert t001000000_x15()
                """State 39"""
                # talk:999000000:"No new messages."
                assert t001000000_x46(text1=999000000, z1=91000060)
                """State 18"""
                # eventflag:3441:	[Garage] Judgment by seeing the story production_Chapter 5 progress 2 	【ガレージ】ストーリー演出を見た判定_チャプター5進行度2
                SetEventFlag(3441, 1)
                """State 52"""
                return 6
            else:
                """State 2"""
                # eventflag:3442:	[Garage] Judgment by seeing the story production_Chapter 5 progress 3 	【ガレージ】ストーリー演出を見た判定_チャプター5進行度3, mission:5020:"Intercept the Corporate Forces"
                if not GetEventFlag(3442) and UnkMissionComplete(5020, 1) == 1:
                    """State 3,27"""
                    assert t001000000_x15()
                    """State 40"""
                    # talk:999006000:"Incoming comms."
                    assert t001000000_x46(text1=999006000, z1=91000060)
                    """State 28"""
                    # talk:960100010:"Just went to say goodbye to Chatty."
                    assert t001000000_x33(text3=960100010, z3=91000040)
                    """State 4"""
                    # eventflag:3442:	[Garage] Judgment by seeing the story production_Chapter 5 progress 3 	【ガレージ】ストーリー演出を見た判定_チャプター5進行度3
                    SetEventFlag(3442, 1)
                    UnkUnlockDecal(6600)
                    """State 48"""
                    c1_230(0)
                    return 2
                else:
                    """State 5"""
                    # eventflag:3442:	[Garage] Judgment by seeing the story production_Chapter 5 progress 3 	【ガレージ】ストーリー演出を見た判定_チャプター5進行度3, mission:5050:"Eliminate "Cinder" Carla"
                    if not GetEventFlag(3442) and UnkMissionComplete(5050, 1) == 1:
                        """State 6,29"""
                        assert t001000000_x15()
                        """State 41"""
                        # talk:999000000:"No new messages."
                        assert t001000000_x46(text1=999000000, z1=91000060)
                        """State 30"""
                        # talk:970100010:"...Carla had planned everything,\neven her own death."
                        assert t001000000_x33(text3=970100010, z3=91000030)
                        """State 7"""
                        # eventflag:3442:	[Garage] Judgment by seeing the story production_Chapter 5 progress 3 	【ガレージ】ストーリー演出を見た判定_チャプター5進行度3
                        SetEventFlag(3442, -1)
                        """State 49"""
                        c1_230(0)
                        return 3
                    else:
                        """State 21"""
                        # eventflag:3436:	[Garage] Judgment by seeing the story production_Chapter 4 progress level 7 	【ガレージ】ストーリー演出を見た判定_チャプター4進行度7, mission:4035:"Reach the Coral Convergence"
                        if not GetEventFlag(3436) and UnkMissionComplete(4035, 1) == 1:
                            """State 22,43"""
                            assert t001000000_x15()
                            """State 45"""
                            # talk:999000000:"No new messages."
                            assert t001000000_x46(text1=999000000, z1=91000060)
                            """State 44"""
                            # talk:980000010:"We've received a message from ALLMIND."
                            assert t001000000_x33(text3=980000010, z3=91000030)
                            """State 23"""
                            c1_229(7)
                            # eventflag:3436:	[Garage] Judgment by seeing the story production_Chapter 4 progress level 7 	【ガレージ】ストーリー演出を見た判定_チャプター4進行度7
                            SetEventFlag(3436, 1)
                            """State 53"""
                            return 7
                        else:
                            """State 11"""
                            # eventflag:3443:	[Garage] Judgment by seeing the story production_Chapter 5 progress 4 	【ガレージ】ストーリー演出を見た判定_チャプター5進行度4, mission:5040:"Breach the Kármán Line"
                            if not GetEventFlag(3443) and UnkMissionComplete(5040, 1) == 1:
                                """State 12"""
                                Label('L1')
                                """State 33"""
                                call = t001000000_x15()
                                # eventflag:6523:	Get parts by clearing the atmosphere breakthrough 	大気圏突破クリアでパーツ入手, mission:5040:"Breach the Kármán Line"
                                if (call.Done() and (not GetEventFlag(6523) and UnkMissionComplete(5040,
                                    1) == 1)):
                                    """State 24"""
                                    # protector:50080200:EL-PH-00 ALBA
                                    GiveItemDirectly(1, 50080200, 1)
                                    # protector:51080200:EL-PC-00 ALBA
                                    GiveItemDirectly(1, 51080200, 1)
                                    # protector:52080200:EL-PA-00 ALBA
                                    GiveItemDirectly(1, 52080200, 1)
                                    # protector:53080200:EL-PL-00 ALBA
                                    GiveItemDirectly(1, 53080200, 1)
                                    # eventflag:6523:	Get parts by clearing the atmosphere breakthrough 	大気圏突破クリアでパーツ入手
                                    SetEventFlag(6523, 1)
                                    assert f338() == 1
                                elif call.Done():
                                    pass
                                """State 42"""
                                # talk:999005000:"Augmented human C4-621: Entering Standard Mode."
                                assert t001000000_x46(text1=999005000, z1=91000060)
                                """State 13"""
                                # eventflag:3443:	[Garage] Judgment by seeing the story production_Chapter 5 progress 4 	【ガレージ】ストーリー演出を見た判定_チャプター5進行度4
                                SetEventFlag(3443, 1)
                                """State 51"""
                                c1_230(0)
                                return 5
                            # mission:5030:"Destroy the Drive Block", eventflag:3443:	[Garage] Judgment by seeing the story production_Chapter 5 progress 4 	【ガレージ】ストーリー演出を見た判定_チャプター5進行度4
                            elif UnkMissionComplete(5030, 1) == 1 and not GetEventFlag(3443):
                                Goto('L1')
                            # mission:5110:"Regain Control of the Xylem", eventflag:3443:	[Garage] Judgment by seeing the story production_Chapter 5 progress 4 	【ガレージ】ストーリー演出を見た判定_チャプター5進行度4
                            elif UnkMissionComplete(5110, 1) == 1 and not GetEventFlag(3443):
                                Goto('L1')
                            else:
                                """State 46"""
                                c1_230(0)
                                return 0

def t001000000_x14():
    """State 0,1"""
    c1_230(0)
    # eventflag:8101:	8101_In-mission branching event flag_dam destruction_betrayal route_ 	8101_ミッション内分岐用イベントフラグ_ダム破壊_裏切りルート_
    if GetEventFlag(8101) == 1:
        """State 2"""
        # eventflag:3500:	[Garage] Indigenous flag Dam betrayal 1st PT 	【ガレージ】土着フラグ　ダム裏切り1PT目
        SetEventFlag(3500, 1)
        # eventflag:3501:	[Garage] Indigenous flag Dam betrayal 2nd PT 	【ガレージ】土着フラグ　ダム裏切り2PT目
        SetEventFlag(3501, 1)
    else:
        pass
    """State 3"""
    # mission:7910:"Prevent Corporate Salvage of New Tech"
    if UnkMissionComplete(7910, 1) == 1:
        """State 4"""
        # eventflag:3502:	[Garage] Indigenous Flag Sabumi: 1st clearing of open-air quarry 	【ガレージ】土着フラグ　サブミ：露天採掘場クリア1PT目
        SetEventFlag(3502, 1)
        # eventflag:3503:	[Garage] Indigenous Flag Sabumi: 2nd Pt. 	【ガレージ】土着フラグ　サブミ：露天採掘場クリア2PT目
        SetEventFlag(3503, 1)
    else:
        pass
    """State 5"""
    # eventflag:8103:	8103 _ Event flag for branching in mission _ Search in front of wall _ Route A (don't miss it) 	8103_ミッション内分岐用イベントフラグ_壁前探索_ルートA（見逃さない）
    if GetEventFlag(8103) == -1:
        """State 6"""
        # eventflag:3504:	[Garage] Indigenous flag Do not accept begging for life in front of the wall 	【ガレージ】土着フラグ　壁前命乞いを受け入れない
        SetEventFlag(3504, 1)
    else:
        pass
    """State 7"""
    # mission:2220:"Heavy Missile Launch Support"
    if UnkMissionComplete(2220, 1) == 1:
        """State 8"""
        # eventflag:3505:	[Garage] Indigenous flag Unknown aircraft elimination cleared 	【ガレージ】土着フラグ　不明機体排除クリア
        SetEventFlag(3505, 1)
    else:
        pass
    """State 9"""
    # mission:4110:"Ambush the Vespers"
    if UnkMissionComplete(4110, 1) == 1:
        """State 10"""
        # eventflag:3506:	[Garage] Indigenous flag AC battle clear at the power plant 	【ガレージ】土着フラグ　発電所でのAC戦クリア
        SetEventFlag(3506, 1)
    else:
        pass
    """State 11"""
    StartEvent(0, 3600)
    """State 12"""
    # mission:4026:"Unknown Territory Survey"
    if UnkMissionComplete(4026, 1) == 1:
        """State 13"""
        # eventflag:3601:	[Garage] Flag to go to route B (Bioweapon ALT clear) 	【ガレージ】Bルートに行けるフラグ(生体兵器ALTクリア)
        SetEventFlag(3601, 1)
    else:
        pass
    """State 15"""
    return 1
    """Unused"""
    """State 14"""
    return 0

def t001000000_x15():
    """State 0"""
    assert GetCurrentStateElapsedTime() > 2
    """State 1"""
    return 0

def t001000000_x16():
    """State 0,1"""
    # eventflag:6210:	Mining Ship & Dam Destruction 	採掘艦＆ダム破壊
    SetEventFlag(6210, 1)
    c1_230(0)
    c1_229(7)
    """State 2,3"""
    # tutorial:2100010:Products Updated: PARTS SHOP
    ShowTutorialMessage(2100010)
    assert (not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            and GetCurrentStateElapsedFrames() > 1)
    """State 4"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    return 0

def t001000000_x17():
    """State 0,1"""
    c1_230(0)
    """State 2,3"""
    # tutorial:2103020:Training Exercises Updated: TRAINING
    ShowTutorialMessage(2103020)
    # mission:9201:"Beginner Training 2: Combat Fundamentals"
    SetMissionState(9201, 0, 1)
    assert (not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            and GetCurrentStateElapsedFrames() > 1)
    """State 4"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    return 0

def t001000000_x18():
    """State 0,1"""
    c1_230(0)
    """State 2,3"""
    # tutorial:2103020:Training Exercises Updated: TRAINING
    ShowTutorialMessage(2103020)
    # mission:9202:"Intermediate Support 1: Assembling an AC"
    SetMissionState(9202, 0, 1)
    # mission:9203:"Intermediate Support 2: Reverse-Jointed ACs"
    SetMissionState(9203, 0, 1)
    assert (not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            and GetCurrentStateElapsedFrames() > 1)
    """State 4"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    return 0

def t001000000_x19():
    """State 0,1"""
    # eventflag:6220:	over the wall 	壁越え
    SetEventFlag(6220, 1)
    c1_230(0)
    c1_229(7)
    """State 2,3"""
    # tutorial:2100010:Products Updated: PARTS SHOP
    ShowTutorialMessage(2100010)
    assert (not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            and GetCurrentStateElapsedFrames() > 1)
    """State 4"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    return 0

def t001000000_x20():
    """State 0,1"""
    # eventflag:6230:	the coordinates indicated by the string 	文字列が示す座標
    SetEventFlag(6230, 1)
    c1_230(0)
    c1_229(7)
    """State 2,3"""
    # tutorial:2100010:Products Updated: PARTS SHOP
    ShowTutorialMessage(2100010)
    assert (not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            and GetCurrentStateElapsedFrames() > 1)
    """State 4"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    return 0

def t001000000_x21():
    """State 0,1"""
    # eventflag:6240:	continental crust 	大陸殻
    SetEventFlag(6240, 1)
    c1_230(0)
    c1_229(7)
    """State 2,3"""
    # tutorial:2100010:Products Updated: PARTS SHOP
    ShowTutorialMessage(2100010)
    assert (not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            and GetCurrentStateElapsedFrames() > 1)
    """State 4"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    return 0

def t001000000_x22():
    """State 0,1"""
    # eventflag:6250:	Defeat Iceworm 	アイスワーム撃破
    SetEventFlag(6250, 1)
    c1_230(0)
    c1_229(7)
    SetEventFlag(6245, 1)
    """State 2,3"""
    # tutorial:2100010:Products Updated: PARTS SHOP
    ShowTutorialMessage(2100010)
    assert (not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            and GetCurrentStateElapsedFrames() > 1)
    """State 4"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    return 0

def t001000000_x23():
    """State 0,1"""
    # eventflag:6260:	prison break 	脱獄
    SetEventFlag(6260, 1)
    c1_230(0)
    c1_229(7)
    SetEventFlag(6245, 1)
    """State 2,3"""
    # tutorial:2100010:Products Updated: PARTS SHOP
    ShowTutorialMessage(2100010)
    assert (not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            and GetCurrentStateElapsedFrames() > 1)
    """State 4"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    return 0

def t001000000_x24():
    """State 0,1"""
    # eventflag:6275:	Continental crust: 2nd lap 	大陸殻：２周目
    SetEventFlag(6275, 1)
    c1_230(0)
    c1_229(7)
    SetEventFlag(6245, 1)
    """State 2,3"""
    # tutorial:2100010:Products Updated: PARTS SHOP
    ShowTutorialMessage(2100010)
    assert (not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            and GetCurrentStateElapsedFrames() > 1)
    """State 4"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    return 0

def t001000000_x25():
    """State 0,1"""
    # eventflag:6280:	Defeat Iceworm: Round 2 	アイスワーム撃破：２周目
    SetEventFlag(6280, 1)
    c1_230(0)
    c1_229(7)
    SetEventFlag(6245, 1)
    """State 2,3"""
    # tutorial:2100010:Products Updated: PARTS SHOP
    ShowTutorialMessage(2100010)
    assert (not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            and GetCurrentStateElapsedFrames() > 1)
    """State 4"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    return 0

def t001000000_x26():
    """State 0,1"""
    c1_230(0)
    """State 2,3"""
    # mission:9200:"Beginner Training 1: Basic Controls"
    SetMissionState(9200, 0, 1)
    assert (not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            and GetCurrentStateElapsedFrames() > 1)
    """State 4"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    return 0

def t001000000_x27():
    """State 0,1"""
    # eventflag:6050:	Complete Arena F 	アリーナF完遂
    if (UnkArenaComplete(101) == 1 and UnkArenaComplete(102) == 1 and UnkArenaComplete(100) == 1 and
        not GetEventFlag(6050)):
        pass
    else:
        Goto('L0')
    """State 15"""
    # eventflag:3447:	[Garage] Current Route C 	【ガレージ】現在Cルート
    if GetEventFlag(3447) == 1:
        """State 16"""
        # eventflag:3448:	[Garage] I just saw the start of the arena 	【ガレージ】今更アリーナ開始見た
        if not GetEventFlag(3448):
            """State 77"""
            # talk:999006000:"Incoming comms."
            assert t001000000_x46(text1=999006000, z1=91000060)
            """State 78"""
            # talk:992002010:"Augmented human C4-621—Raven."
            assert t001000000_x33(text3=992002010, z3=91000010)
            """State 38"""
            # eventflag:3448:	[Garage] I just saw the start of the arena 	【ガレージ】今更アリーナ開始見た
            SetEventFlag(3448, 1)
        # eventflag:3448:	[Garage] I just saw the start of the arena 	【ガレージ】今更アリーナ開始見た
        elif GetEventFlag(3448) == 1:
            pass
    else:
        """State 70"""
        # talk:999006000:"Incoming comms."
        assert t001000000_x46(text1=999006000, z1=91000060)
        """State 63"""
        # talk:990100010:"Congratulations. You have surpassed Rank F."
        assert t001000000_x33(text3=990100010, z3=91000010)
    """State 2"""
    # eventflag:6050:	Complete Arena F 	アリーナF完遂
    SetEventFlag(6050, 1)
    """State 111"""
    return 1
    """State 3"""
    Label('L0')
    # eventflag:6051:	Complete Arena E 	アリーナE完遂
    if (UnkArenaComplete(103) == 1 and UnkArenaComplete(104) == 1 and UnkArenaComplete(105) == 1 and
        not GetEventFlag(6051) and UnkArenaComplete(106) == 1):
        pass
    else:
        Goto('L1')
    """State 17"""
    # eventflag:3447:	[Garage] Current Route C 	【ガレージ】現在Cルート
    if GetEventFlag(3447) == 1:
        """State 18"""
        # eventflag:3448:	[Garage] I just saw the start of the arena 	【ガレージ】今更アリーナ開始見た
        if not GetEventFlag(3448):
            """State 79"""
            # talk:999006000:"Incoming comms."
            assert t001000000_x46(text1=999006000, z1=91000060)
            """State 80"""
            # talk:992002010:"Augmented human C4-621—Raven."
            assert t001000000_x33(text3=992002010, z3=91000010)
            """State 39"""
            # eventflag:3448:	[Garage] I just saw the start of the arena 	【ガレージ】今更アリーナ開始見た
            SetEventFlag(3448, 1)
        else:
            pass
    else:
        """State 71"""
        # talk:999006000:"Incoming comms."
        assert t001000000_x46(text1=999006000, z1=91000060)
        """State 64"""
        # talk:990200010:"Congratulations. You have surpassed Rank E."
        assert t001000000_x33(text3=990200010, z3=91000010)
    """State 4"""
    # eventflag:6051:	Complete Arena E 	アリーナE完遂
    SetEventFlag(6051, 1)
    """State 112"""
    return 2
    """State 5"""
    Label('L1')
    # eventflag:6052:	Complete Arena D 	アリーナD完遂
    if (UnkArenaComplete(107) == 1 and UnkArenaComplete(108) == 1 and UnkArenaComplete(109) == 1 and
        not GetEventFlag(6052) and UnkArenaComplete(110) == 1 and UnkArenaComplete(111) == 1):
        pass
    else:
        Goto('L2')
    """State 40"""
    # eventflag:3447:	[Garage] Current Route C 	【ガレージ】現在Cルート
    if GetEventFlag(3447) == 1:
        """State 41"""
        # eventflag:3448:	[Garage] I just saw the start of the arena 	【ガレージ】今更アリーナ開始見た
        if not GetEventFlag(3448):
            """State 98"""
            # talk:999006000:"Incoming comms."
            assert t001000000_x46(text1=999006000, z1=91000060)
            """State 99"""
            # talk:992002010:"Augmented human C4-621—Raven."
            assert t001000000_x33(text3=992002010, z3=91000010)
            """State 42"""
            # eventflag:3448:	[Garage] I just saw the start of the arena 	【ガレージ】今更アリーナ開始見た
            SetEventFlag(3448, 1)
        else:
            pass
    else:
        """State 72"""
        # talk:999006000:"Incoming comms."
        assert t001000000_x46(text1=999006000, z1=91000060)
        """State 65"""
        # talk:990300010:"Congratulations. You have surpassed Rank D."
        assert t001000000_x33(text3=990300010, z3=91000010)
    """State 6"""
    # eventflag:6052:	Complete Arena D 	アリーナD完遂
    SetEventFlag(6052, 1)
    """State 113"""
    return 3
    """State 7"""
    Label('L2')
    # eventflag:6053:	Complete Arena C 	アリーナC完遂
    if (UnkArenaComplete(112) == 1 and UnkArenaComplete(113) == 1 and UnkArenaComplete(114) == 1 and
        not GetEventFlag(6053) and UnkArenaComplete(115) == 1 and UnkArenaComplete(116) == 1):
        pass
    else:
        Goto('L3')
    """State 43"""
    # eventflag:3447:	[Garage] Current Route C 	【ガレージ】現在Cルート
    if GetEventFlag(3447) == 1:
        """State 44"""
        # eventflag:3448:	[Garage] I just saw the start of the arena 	【ガレージ】今更アリーナ開始見た
        if not GetEventFlag(3448):
            """State 100"""
            # talk:999006000:"Incoming comms."
            assert t001000000_x46(text1=999006000, z1=91000060)
            """State 101"""
            # talk:992002010:"Augmented human C4-621—Raven."
            assert t001000000_x33(text3=992002010, z3=91000010)
            """State 52"""
            # eventflag:3448:	[Garage] I just saw the start of the arena 	【ガレージ】今更アリーナ開始見た
            SetEventFlag(3448, 1)
        else:
            pass
    else:
        """State 73"""
        # talk:999006000:"Incoming comms."
        assert t001000000_x46(text1=999006000, z1=91000060)
        """State 66"""
        # talk:990400010:"Congratulations. You have surpassed Rank C."
        assert t001000000_x33(text3=990400010, z3=91000010)
    """State 8"""
    # eventflag:6053:	Complete Arena C 	アリーナC完遂
    SetEventFlag(6053, 1)
    """State 114"""
    return 4
    """State 9"""
    Label('L3')
    # eventflag:6054:	Complete Arena B 	アリーナB完遂
    if (UnkArenaComplete(117) == 1 and UnkArenaComplete(118) == 1 and UnkArenaComplete(119) == 1 and
        UnkArenaComplete(120) == 1 and UnkArenaComplete(121) == 1 and not GetEventFlag(6054)):
        pass
    else:
        Goto('L4')
    """State 45"""
    # eventflag:3447:	[Garage] Current Route C 	【ガレージ】現在Cルート
    if GetEventFlag(3447) == 1:
        """State 46"""
        # eventflag:3448:	[Garage] I just saw the start of the arena 	【ガレージ】今更アリーナ開始見た
        if not GetEventFlag(3448):
            """State 102"""
            # talk:999006000:"Incoming comms."
            assert t001000000_x46(text1=999006000, z1=91000060)
            """State 103"""
            # talk:992002010:"Augmented human C4-621—Raven."
            assert t001000000_x33(text3=992002010, z3=91000010)
            """State 47"""
            # eventflag:3448:	[Garage] I just saw the start of the arena 	【ガレージ】今更アリーナ開始見た
            SetEventFlag(3448, 1)
        else:
            pass
    else:
        """State 74"""
        # talk:999006000:"Incoming comms."
        assert t001000000_x46(text1=999006000, z1=91000060)
        """State 67"""
        # talk:990500010:"Congratulations. You have surpassed Rank B."
        assert t001000000_x33(text3=990500010, z3=91000010)
    """State 10"""
    # eventflag:6054:	Complete Arena B 	アリーナB完遂
    SetEventFlag(6054, 1)
    """State 115"""
    return 5
    """State 12"""
    Label('L4')
    # eventflag:6055:	Complete Arena A 	アリーナA完遂
    if (UnkArenaComplete(122) == 1 and UnkArenaComplete(123) == 1 and UnkArenaComplete(124) == 1 and
        UnkArenaComplete(125) == 1 and not GetEventFlag(6055)):
        pass
    else:
        Goto('L5')
    """State 48"""
    # eventflag:3447:	[Garage] Current Route C 	【ガレージ】現在Cルート
    if GetEventFlag(3447) == 1:
        """State 49"""
        # eventflag:3448:	[Garage] I just saw the start of the arena 	【ガレージ】今更アリーナ開始見た
        if not GetEventFlag(3448):
            """State 105"""
            # talk:999006000:"Incoming comms."
            assert t001000000_x46(text1=999006000, z1=91000060)
            """State 104"""
            # talk:992002010:"Augmented human C4-621—Raven."
            assert t001000000_x33(text3=992002010, z3=91000010)
            """State 53"""
            # eventflag:3448:	[Garage] I just saw the start of the arena 	【ガレージ】今更アリーナ開始見た
            SetEventFlag(3448, 1)
        else:
            pass
    else:
        """State 75"""
        # talk:999006000:"Incoming comms."
        assert t001000000_x46(text1=999006000, z1=91000060)
        """State 68"""
        # talk:990600010:"Congratulations. You have surpassed Rank A."
        assert t001000000_x33(text3=990600010, z3=91000010)
    """State 11"""
    # eventflag:6055:	Complete Arena A 	アリーナA完遂
    SetEventFlag(6055, 1)
    """State 116"""
    return 6
    """State 13"""
    Label('L5')
    # eventflag:6056:	Complete Arena S 	アリーナS完遂
    if (UnkArenaComplete(126) == 1 and UnkArenaComplete(127) == 1 and UnkArenaComplete(128) == 1 and
        not GetEventFlag(6056)):
        pass
    else:
        Goto('L6')
    """State 76"""
    # talk:999006000:"Incoming comms."
    call = t001000000_x46(text1=999006000, z1=91000060)
    # eventflag:3447:	[Garage] Current Route C 	【ガレージ】現在Cルート
    if call.Done() and GetEventFlag(3447) == 1:
        """State 37,97"""
        # talk:992003010:"Your conquest of the arena ranks has been confirmed.\nCongratulations."
        assert t001000000_x33(text3=992003010, z3=91000010)
    elif call.Done():
        """State 69"""
        # talk:990700010:"Congratulations. You have completed all ranks."
        assert t001000000_x33(text3=990700010, z3=91000010)
    """State 62"""
    # tutorial:2107020:Certification: Evaluation Complete
    ShowTutorialMessage(2107020)
    assert (not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            and GetCurrentStateElapsedFrames() > 1)
    """State 14"""
    UnkUnlockDecal(6056)
    """State 117"""
    return 7
    """State 19"""
    Label('L6')
    # eventflag:6057:	Alpha simulator completed 	αシミュレーター完遂
    if (UnkArenaComplete(200) == 1 and UnkArenaComplete(201) == 1 and not GetEventFlag(6057) and UnkArenaComplete(202)
        == 1):
        pass
    else:
        Goto('L7')
    """State 50"""
    # eventflag:3447:	[Garage] Current Route C 	【ガレージ】現在Cルート
    if GetEventFlag(3447) == 1:
        """State 51"""
        # eventflag:3449:	[Garage] Arena now open 	【ガレージ】今更アリーナ開
        if not GetEventFlag(3449):
            """State 106"""
            # talk:999006000:"Incoming comms."
            assert t001000000_x46(text1=999006000, z1=91000060)
            """State 107"""
            # talk:992004010:"Augmented human C4-621—Raven."
            assert t001000000_x33(text3=992004010, z3=91000010)
            """State 54"""
            # eventflag:3449:	[Garage] Arena now open 	【ガレージ】今更アリーナ開
            SetEventFlag(3449, 1)
        else:
            pass
    else:
        """State 81"""
        # talk:999006000:"Incoming comms."
        assert t001000000_x46(text1=999006000, z1=91000060)
        """State 82"""
        # talk:991100010:"Thank you for your continued support."
        assert t001000000_x33(text3=991100010, z3=91000010)
    """State 27"""
    # eventflag:6057:	Alpha simulator completed 	αシミュレーター完遂
    SetEventFlag(6057, 1)
    """State 118"""
    return 8
    """State 20"""
    Label('L7')
    # eventflag:6058:	Beta simulator completed 	βシミュレーター完遂
    if (UnkArenaComplete(203) == 1 and UnkArenaComplete(204) == 1 and not GetEventFlag(6058) and UnkArenaComplete(205)
        == 1):
        pass
    else:
        Goto('L8')
    """State 55"""
    # eventflag:3447:	[Garage] Current Route C 	【ガレージ】現在Cルート
    if GetEventFlag(3447) == 1:
        """State 56"""
        # eventflag:3449:	[Garage] Arena now open 	【ガレージ】今更アリーナ開
        if not GetEventFlag(3449):
            """State 108"""
            # talk:999006000:"Incoming comms."
            assert t001000000_x46(text1=999006000, z1=91000060)
            """State 109"""
            # talk:992004010:"Augmented human C4-621—Raven."
            assert t001000000_x33(text3=992004010, z3=91000010)
            """State 57"""
            # eventflag:3449:	[Garage] Arena now open 	【ガレージ】今更アリーナ開
            SetEventFlag(3449, 1)
        else:
            pass
    else:
        """State 83"""
        # talk:999006000:"Incoming comms."
        assert t001000000_x46(text1=999006000, z1=91000060)
        """State 84"""
        # talk:991200010:"Thank you for your continued support."
        assert t001000000_x33(text3=991200010, z3=91000010)
    """State 28"""
    # eventflag:6058:	Beta simulator completed 	βシミュレーター完遂
    SetEventFlag(6058, 1)
    """State 119"""
    return 9
    """State 21"""
    Label('L8')
    # eventflag:6059:	Completion of γ simulator 	γシミュレーター完遂
    if (UnkArenaComplete(206) == 1 and UnkArenaComplete(207) == 1 and not GetEventFlag(6059) and UnkArenaComplete(208)
        == 1):
        pass
    else:
        Goto('L9')
    """State 85"""
    # talk:999006000:"Incoming comms."
    call = t001000000_x46(text1=999006000, z1=91000060)
    # eventflag:3447:	[Garage] Current Route C 	【ガレージ】現在Cルート
    if call.Done() and GetEventFlag(3447) == 1:
        """State 36,96"""
        # talk:992005010:"The Integration Program has come to a close.\nYou have our thanks."
        assert t001000000_x33(text3=992005010, z3=91000010)
    elif call.Done():
        """State 86"""
        # talk:991300010:"Thank you for your continued support."
        assert t001000000_x33(text3=991300010, z3=91000010)
    """State 61"""
    # tutorial:2107030:Certification: Integration Complete
    ShowTutorialMessage(2107030)
    assert (not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            and GetCurrentStateElapsedFrames() > 1)
    """State 29"""
    UnkUnlockDecal(6059)
    """State 120"""
    return 10
    """State 22"""
    Label('L9')
    # eventflag:6060:	Defeat Rusty Simulator 	ラスティシミュレーター撃破
    if not GetEventFlag(6060) and UnkArenaComplete(209) == 1:
        pass
    else:
        Goto('L10')
    """State 87"""
    # talk:991400010:"What do you think ALLMIND\nis collecting all this data for?"
    assert t001000000_x33(text3=991400010, z3=91000030)
    """State 30"""
    # eventflag:6060:	Defeat Rusty Simulator 	ラスティシミュレーター撃破
    SetEventFlag(6060, 1)
    UnkUnlockDecal(6612)
    """State 121"""
    return 11
    """State 23"""
    Label('L10')
    # eventflag:6061:	Defeat Walter Simulator 	ウォルターシミュレーター撃破
    if not GetEventFlag(6061) and UnkArenaComplete(210) == 1:
        pass
    else:
        Goto('L11')
    """State 88"""
    # talk:991500010:"That machine... It clearly used Coral technology."
    assert t001000000_x33(text3=991500010, z3=91000030)
    """State 31"""
    # eventflag:6061:	Defeat Walter Simulator 	ウォルターシミュレーター撃破
    SetEventFlag(6061, 1)
    UnkUnlockDecal(6613)
    """State 122"""
    return 12
    """State 24"""
    Label('L11')
    # eventflag:6062:	Defeat Air 	エア撃破
    if not GetEventFlag(6062) and UnkArenaComplete(211) == 1:
        pass
    else:
        Goto('L12')
    """State 89"""
    # talk:991600010:"That was incredible, Raven."
    assert t001000000_x33(text3=991600010, z3=91000030)
    """State 32"""
    UnkUnlockDecal(6062)
    """State 123"""
    return 13
    """State 25"""
    Label('L12')
    # eventflag:6415:	Reach Mercenary Rank 15 	傭兵ランク１５到達
    if not GetEventFlag(6415) and GetMercenaryRank() > 15:
        pass
    else:
        Goto('L13')
    """State 90"""
    # talk:999006000:"Incoming comms."
    call = t001000000_x46(text1=999006000, z1=91000060)
    # mission:5110:"Regain Control of the Xylem"
    if call.Done() and UnkMissionComplete(5110, 1) == 1:
        """State 35,95"""
        # talk:992001010:"Augmented human C4-621—Raven."
        assert t001000000_x33(text3=992001010, z3=91000010)
    elif call.Done():
        """State 91"""
        # talk:992000010:"Registration number Rb23, callsign Raven."
        assert t001000000_x33(text3=992000010, z3=91000010)
    """State 59"""
    # tutorial:2107010:Certification: Elite Hunter
    ShowTutorialMessage(2107010)
    assert (not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            and GetCurrentStateElapsedFrames() > 1)
    """State 58"""
    UnkUnlockDecal(6415)
    """State 124"""
    return 14
    """State 26"""
    Label('L13')
    # eventflag:6437:	clear tremo 7 	トレモ７クリア, mission:9206:"Advanced Mercenary Certification"
    if not GetEventFlag(6437) and UnkMissionComplete(9206, 1) == 1:
        pass
    else:
        Goto('L14')
    """State 92"""
    # talk:999006000:"Incoming comms."
    call = t001000000_x46(text1=999006000, z1=91000060)
    # eventflag:3447:	[Garage] Current Route C 	【ガレージ】現在Cルート
    if call.Done() and GetEventFlag(3447) == 1:
        """State 33,94"""
        # talk:910004010:"Augmented human C4-621—Raven."
        assert t001000000_x33(text3=910004010, z3=91000010)
    elif call.Done():
        """State 93"""
        # talk:910003010:"Congratulations on your certification."
        assert t001000000_x33(text3=910003010, z3=91000010)
        """State 60"""
        # tutorial:2107000:Certification: Advanced Mercenary
        ShowTutorialMessage(2107000)
        assert (not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
                and GetCurrentStateElapsedFrames() > 1)
    """State 34"""
    UnkUnlockDecal(6437)
    """State 125"""
    return 15
    """State 110"""
    Label('L14')
    return 0

def t001000000_x28():
    """State 0,1"""
    c1_230(0)
    c1_229(7)
    # eventflag:3156:	Arena unlock progress 7 	アリーナ解禁進行度7
    SetEventFlag(3156, 1)
    """State 2,3"""
    # tutorial:2101030:New Category Added: ARENA
    ShowTutorialMessage(2101030)
    assert (not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            and GetCurrentStateElapsedFrames() > 1)
    """State 4"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    return 0

def t001000000_x29():
    """State 0,1"""
    c1_230(0)
    c1_229(7)
    # eventflag:3157:	Arena unlock progress 8 	アリーナ解禁進行度8
    SetEventFlag(3157, 1)
    """State 2,3"""
    # tutorial:2101040:Verification Data Updated: ARENA
    ShowTutorialMessage(2101040)
    assert (not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            and GetCurrentStateElapsedFrames() > 1)
    """State 4"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    return 0

def t001000000_x30():
    """State 0,1"""
    c1_230(0)
    c1_229(7)
    """State 2,3"""
    # tutorial:2103000:Access Granted: SORTIE
    ShowTutorialMessage(2103000)
    assert (not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            and GetCurrentStateElapsedFrames() > 1)
    """State 4"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    return 0

def t001000000_x31():
    """State 0,78"""
    if UnkGameCycle() > 1:
        """State 79"""
        Label('L0')
        if GetEventFlag(6245) == 1:
            pass
        else:
            """State 81"""
            assert t001000000_x50()
    # mission:5100:"Survey the Uninhabited Floating City", mission:3430:"Destroy the Special Forces Craft", mission:2220:"Heavy Missile Launch Support"
    elif (UnkMissionComplete(5100, 1) == 1 and UnkMissionComplete(3430, 1) == 1 and UnkMissionComplete(2220,
          1) == 1):
        Goto('L0')
    # mission:5105:"Survey the Uninhabited Floating City", mission:2220:"Heavy Missile Launch Support", mission:3430:"Destroy the Special Forces Craft"
    elif (UnkMissionComplete(5105, 1) == 1 and UnkMissionComplete(2220, 1) == 1 and UnkMissionComplete(3430,
          1) == 1):
        Goto('L0')
    # mission:5100:"Survey the Uninhabited Floating City", mission:2220:"Heavy Missile Launch Support", mission:7990:"Eliminate the Enforcement Squads"
    elif (UnkMissionComplete(5100, 1) == 1 and UnkMissionComplete(2220, 1) == 1 and UnkMissionComplete(7990,
          1) == 1):
        Goto('L0')
    # mission:5105:"Survey the Uninhabited Floating City", mission:2220:"Heavy Missile Launch Support", mission:7990:"Eliminate the Enforcement Squads"
    elif (UnkMissionComplete(5105, 1) == 1 and UnkMissionComplete(2220, 1) == 1 and UnkMissionComplete(7990,
          1) == 1):
        Goto('L0')
    else:
        pass
    """State 1"""
    # eventflag:6431:	Tremo 1 clear 	トレモ１クリア, mission:9200:"Beginner Training 1: Basic Controls"
    if not GetEventFlag(6431) and UnkMissionComplete(9200, 1) == 1:
        """State 2"""
        # eventflag:6431:	Tremo 1 clear 	トレモ１クリア
        SetEventFlag(6431, 1)
        # weapon:10020100:MG-014 LUDLOW
        GiveItemDirectly(0, 10020100, 1)
    else:
        pass
    """State 3"""
    # eventflag:6432:	Tremo 2 clear 	トレモ２クリア, mission:9201:"Beginner Training 2: Combat Fundamentals"
    if not GetEventFlag(6432) and UnkMissionComplete(9201, 1) == 1:
        """State 4"""
        # eventflag:6432:	Tremo 2 clear 	トレモ２クリア
        SetEventFlag(6432, 1)
        # weapon:10000100:LR-036 CURTIS
        GiveItemDirectly(0, 10000100, 1)
    else:
        pass
    """State 5"""
    # eventflag:6433:	Tremo 3 clear 	トレモ３クリア, mission:9202:"Intermediate Support 1: Assembling an AC"
    if not GetEventFlag(6433) and UnkMissionComplete(9202, 1) == 1:
        """State 6"""
        # eventflag:6433:	Tremo 3 clear 	トレモ３クリア
        SetEventFlag(6433, 1)
        # booster:60020000:ALULA/21E
        GiveItemDirectly(6, 60020000, 1)
        # fcs:70010300:FC-006 ABBOT
        GiveItemDirectly(7, 70010300, 1)
        # generator:65010200:VP-20S
        GiveItemDirectly(5, 65010200, 1)
    else:
        pass
    """State 7"""
    # eventflag:6434:	Clear Tremo 4 	トレモ４クリア, mission:9203:"Intermediate Support 2: Reverse-Jointed ACs"
    if not GetEventFlag(6434) and UnkMissionComplete(9203, 1) == 1:
        """State 8"""
        # eventflag:6434:	Clear Tremo 4 	トレモ４クリア
        SetEventFlag(6434, 1)
        # weapon:10110000:VP-66LH
        GiveItemDirectly(0, 10110000, 1)
    else:
        pass
    """State 9"""
    # eventflag:6435:	clear tremo 5 	トレモ５クリア, mission:9204:"Intermediate Support 3: Tetrapod ACs"
    if not GetEventFlag(6435) and UnkMissionComplete(9204, 1) == 1:
        """State 10"""
        # eventflag:6435:	clear tremo 5 	トレモ５クリア
        SetEventFlag(6435, 1)
        # weapon:15060000:DF-GR-07 GOU-CHEN
        GiveItemDirectly(0, 15060000, 1)
    else:
        pass
    """State 11"""
    # eventflag:6436:	clear tremo 6 	トレモ６クリア, mission:9205:"Intermediate Support 4: Tank ACs"
    if not GetEventFlag(6436) and UnkMissionComplete(9205, 1) == 1:
        """State 12"""
        # eventflag:6436:	clear tremo 6 	トレモ６クリア
        SetEventFlag(6436, 1)
        # weapon:35040200:BML-G1/P01VTC-04
        GiveItemDirectly(0, 35040200, 1)
    else:
        pass
    """State 65"""
    # eventflag:6447:	Arena clear: 01 (S) 	アリーナクリア：01(S)
    if not GetEventFlag(6447) and UnkArenaComplete(128) == 1:
        """State 66"""
        # eventflag:6447:	Arena clear: 01 (S) 	アリーナクリア：01(S)
        SetEventFlag(6447, 1)
    else:
        pass
    """State 67"""
    # eventflag:6448:	Arena clear: TEST-09 [γ3] 	アリーナクリア：TEST-09【γ3】
    if not GetEventFlag(6448) and UnkArenaComplete(208) == 1:
        """State 68"""
        # eventflag:6448:	Arena clear: TEST-09 [γ3] 	アリーナクリア：TEST-09【γ3】
        SetEventFlag(6448, 1)
    else:
        pass
    """State 69"""
    # eventflag:6449:	Arena clear: TEST-R [δ1] 	アリーナクリア：TEST-R【δ1】
    if not GetEventFlag(6449) and UnkArenaComplete(209) == 1:
        """State 70"""
        # eventflag:6449:	Arena clear: TEST-R [δ1] 	アリーナクリア：TEST-R【δ1】
        SetEventFlag(6449, 1)
    else:
        pass
    """State 13"""
    # eventflag:6450:	Arena clear: TEST-W [δ2] 	アリーナクリア：TEST-W【δ2】
    if not GetEventFlag(6450) and UnkArenaComplete(210) == 1:
        """State 14"""
        # eventflag:6061:	Defeat Walter Simulator 	ウォルターシミュレーター撃破
        SetEventFlag(6061, 1)
        # eventflag:6450:	Arena clear: TEST-W [δ2] 	アリーナクリア：TEST-W【δ2】
        SetEventFlag(6450, 1)
    else:
        pass
    """State 71"""
    # eventflag:6451:	Arena clear: TEST-A [δ3] 	アリーナクリア：TEST-A【δ3】
    if not GetEventFlag(6451) and UnkArenaComplete(211) == 1:
        """State 72"""
        # eventflag:6451:	Arena clear: TEST-A [δ3] 	アリーナクリア：TEST-A【δ3】
        SetEventFlag(6451, 1)
    else:
        pass
    """State 15"""
    # eventflag:6401:	Reach Mercenary Rank 1 	傭兵ランク１到達
    if not GetEventFlag(6401) and GetMercenaryRank() > 1:
        """State 16"""
        # eventflag:6401:	Reach Mercenary Rank 1 	傭兵ランク１到達
        SetEventFlag(6401, 1)
    else:
        pass
    """State 17"""
    # eventflag:6402:	Reach Mercenary Rank 2 	傭兵ランク２到達
    if not GetEventFlag(6402) and GetMercenaryRank() > 2:
        """State 18"""
        # eventflag:6402:	Reach Mercenary Rank 2 	傭兵ランク２到達
        SetEventFlag(6402, 1)
    else:
        pass
    """State 19"""
    # eventflag:6403:	Reach Mercenary Rank 3 	傭兵ランク３到達
    if not GetEventFlag(6403) and GetMercenaryRank() > 3:
        """State 20"""
        # eventflag:6403:	Reach Mercenary Rank 3 	傭兵ランク３到達
        SetEventFlag(6403, 1)
    else:
        pass
    """State 21"""
    # eventflag:6404:	Reach Mercenary Rank 4 	傭兵ランク４到達
    if not GetEventFlag(6404) and GetMercenaryRank() > 4:
        """State 22"""
        # eventflag:6404:	Reach Mercenary Rank 4 	傭兵ランク４到達
        SetEventFlag(6404, 1)
    else:
        pass
    """State 23"""
    # eventflag:6405:	Reach Mercenary Rank 5 	傭兵ランク５到達
    if not GetEventFlag(6405) and GetMercenaryRank() > 5:
        """State 24"""
        # eventflag:6405:	Reach Mercenary Rank 5 	傭兵ランク５到達
        SetEventFlag(6405, 1)
    else:
        pass
    """State 25"""
    # eventflag:6406:	Reach Mercenary Rank 6 	傭兵ランク６到達
    if not GetEventFlag(6406) and GetMercenaryRank() > 6:
        """State 26"""
        # eventflag:6406:	Reach Mercenary Rank 6 	傭兵ランク６到達
        SetEventFlag(6406, 1)
    else:
        pass
    """State 27"""
    # eventflag:6407:	Reach Mercenary Rank 7 	傭兵ランク７到達
    if not GetEventFlag(6407) and GetMercenaryRank() > 7:
        """State 28"""
        # eventflag:6407:	Reach Mercenary Rank 7 	傭兵ランク７到達
        SetEventFlag(6407, 1)
    else:
        pass
    """State 29"""
    # eventflag:6408:	Reach Mercenary Rank 8 	傭兵ランク８到達
    if not GetEventFlag(6408) and GetMercenaryRank() > 8:
        """State 30"""
        # eventflag:6408:	Reach Mercenary Rank 8 	傭兵ランク８到達
        SetEventFlag(6408, 1)
    else:
        pass
    """State 31"""
    # eventflag:6409:	Reach Mercenary Rank 9 	傭兵ランク９到達
    if not GetEventFlag(6409) and GetMercenaryRank() > 9:
        """State 32"""
        # eventflag:6409:	Reach Mercenary Rank 9 	傭兵ランク９到達
        SetEventFlag(6409, 1)
    else:
        pass
    """State 33"""
    # eventflag:6410:	Reach Mercenary Rank 10 	傭兵ランク１０到達
    if not GetEventFlag(6410) and GetMercenaryRank() > 10:
        """State 34"""
        # eventflag:6410:	Reach Mercenary Rank 10 	傭兵ランク１０到達
        SetEventFlag(6410, 1)
    else:
        pass
    """State 35"""
    # eventflag:6411:	Reach Mercenary Rank 11 	傭兵ランク１１到達
    if not GetEventFlag(6411) and GetMercenaryRank() > 11:
        """State 36"""
        # eventflag:6411:	Reach Mercenary Rank 11 	傭兵ランク１１到達
        SetEventFlag(6411, 1)
    else:
        pass
    """State 37"""
    # eventflag:6412:	Reach Mercenary Rank 12 	傭兵ランク１２到達
    if not GetEventFlag(6412) and GetMercenaryRank() > 12:
        """State 38"""
        # eventflag:6412:	Reach Mercenary Rank 12 	傭兵ランク１２到達
        SetEventFlag(6412, 1)
    else:
        pass
    """State 39"""
    # eventflag:6413:	Reach Mercenary Rank 13 	傭兵ランク１３到達
    if not GetEventFlag(6413) and GetMercenaryRank() > 13:
        """State 40"""
        # eventflag:6413:	Reach Mercenary Rank 13 	傭兵ランク１３到達
        SetEventFlag(6413, 1)
    else:
        pass
    """State 41"""
    # eventflag:6414:	Reach Mercenary Rank 14 	傭兵ランク１４到達
    if not GetEventFlag(6414) and GetMercenaryRank() > 14:
        """State 42"""
        # eventflag:6414:	Reach Mercenary Rank 14 	傭兵ランク１４到達
        SetEventFlag(6414, 1)
    else:
        pass
    """State 43"""
    # eventflag:6415:	Reach Mercenary Rank 15 	傭兵ランク１５到達
    if not GetEventFlag(6415) and GetMercenaryRank() > 15:
        """State 44"""
        UnkUnlockDecal(6415)
    else:
        pass
    """State 45"""
    # mission:9206:"Advanced Mercenary Certification"
    if not UnkMissionComplete(9206, 1) == 1 and not UnkMissionComplete(9206, 0) == 1:
        """State 46"""
        # eventflag:6431:	Tremo 1 clear 	トレモ１クリア, eventflag:6432:	Tremo 2 clear 	トレモ２クリア, eventflag:6433:	Tremo 3 clear 	トレモ３クリア, eventflag:6434:	Clear Tremo 4 	トレモ４クリア, eventflag:6435:	clear tremo 5 	トレモ５クリア, eventflag:6436:	clear tremo 6 	トレモ６クリア
        if (GetEventFlag(6431) == 1 and GetEventFlag(6432) == 1 and GetEventFlag(6433) == 1 and GetEventFlag(6434)
            == 1 and GetEventFlag(6435) == 1 and GetEventFlag(6436) == 1):
            """State 80"""
            assert (t001000000_x36() and (not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
                    and GetCurrentStateElapsedFrames() > 1))
        else:
            pass
    else:
        pass
    """State 76"""
    # weapon:30030000:IB-C03W3: NGI 006, eventflag:6461:	straight city invasion 	ストレート市街侵攻
    if ComparePlayerInventoryNumber(0, 30030000, 0, 1, 0) == 1 and not GetEventFlag(6461):
        """State 77"""
        # eventflag:6461:	straight city invasion 	ストレート市街侵攻
        SetEventFlag(6461, 1)
    else:
        pass
    """State 47"""
    # weapon:30350100:IA-C01W3: AURORA, eventflag:6462:	offshore city 	洋上の都市
    if ComparePlayerInventoryNumber(0, 30350100, 0, 1, 0) == 1 and not GetEventFlag(6462):
        """State 48"""
        # eventflag:6462:	offshore city 	洋上の都市
        SetEventFlag(6462, 1)
    else:
        pass
    """State 61"""
    # weapon:10150200:IA-C01W1: NEBULA, eventflag:6463:	Mine sabotage 	坑道破壊工作
    if ComparePlayerInventoryNumber(0, 10150200, 0, 1, 0) == 1 and not GetEventFlag(6463):
        """State 62"""
        # eventflag:6463:	Mine sabotage 	坑道破壊工作
        SetEventFlag(6463, 1)
    else:
        pass
    """State 63"""
    # weapon:10160000:WB-0000 BAD COOK, eventflag:6464:	collapsed continental crust 2 	崩落した大陸殻２
    if ComparePlayerInventoryNumber(0, 10160000, 0, 1, 0) == 1 and not GetEventFlag(6464):
        """State 64"""
        # eventflag:6464:	collapsed continental crust 2 	崩落した大陸殻２
        SetEventFlag(6464, 1)
    else:
        pass
    """State 49"""
    # eventflag:6018:	let the air out even once 	一度でもエアを出した
    if GetEventFlag(6018) == 1:
        """State 50"""
        if not GetChapter():
            """State 51"""
            Label('L1')
            # eventflag:6015:	Arena unlocking progress 6 take over 	アリーナ解禁進行度6　引継ぎ
            SetEventFlag(6015, 0)
            # eventflag:6016:	Arena unlocking progress 7 take over 	アリーナ解禁進行度7　引継ぎ
            SetEventFlag(6016, 0)
            # eventflag:6017:	Arena unlocking progress level 8 takeover 	アリーナ解禁進行度8　引継ぎ
            SetEventFlag(6017, 0)
        # mission:5020:"Intercept the Corporate Forces"
        elif UnkMissionComplete(5020, 1) == 1:
            Goto('L1')
        else:
            """State 52"""
            # eventflag:6015:	Arena unlocking progress 6 take over 	アリーナ解禁進行度6　引継ぎ
            SetEventFlag(6015, 1)
            # eventflag:6016:	Arena unlocking progress 7 take over 	アリーナ解禁進行度7　引継ぎ
            SetEventFlag(6016, 1)
            # eventflag:6017:	Arena unlocking progress level 8 takeover 	アリーナ解禁進行度8　引継ぎ
            SetEventFlag(6017, 1)
    else:
        pass
    """State 53,54"""
    # eventflag:6500:	Collected all information logs 	情報ログをすべて集めた, eventflag:6510:	Obtain a medal for collecting all information logs 	情報ログをすべて集めた勲章入手
    if GetEventFlag(6500) == 1 and not GetEventFlag(6510):
        """State 73"""
        # tutorial:2107070:Certification: Omniscience
        ShowTutorialMessage(2107070)
        assert (not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
                and GetCurrentStateElapsedFrames() > 1)
        """State 58"""
        UnkUnlockDecal(6510)
    else:
        pass
    """State 55"""
    # eventflag:6501:	Cleared all missions 	すべてのミッションをクリアした, eventflag:6511:	Obtain a medal for clearing all missions 	すべてのミッションをクリアした勲章入手
    if GetEventFlag(6501) == 1 and not GetEventFlag(6511):
        """State 74"""
        # tutorial:2107040:Certification: Stargazer
        ShowTutorialMessage(2107040)
        assert (not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
                and GetCurrentStateElapsedFrames() > 1)
        """State 59"""
        UnkUnlockDecal(6511)
    else:
        pass
    """State 56"""
    # eventflag:6502:	Cleared all missions with S rank 	すべてのミッションをSランクでクリアした, eventflag:6512:	Obtain a medal for clearing all missions with S rank. 	すべてのミッションをSランクでクリアした勲章入手
    if GetEventFlag(6502) == 1 and not GetEventFlag(6512):
        """State 75"""
        # tutorial:2107050:Certification: Perfect Mercenary
        ShowTutorialMessage(2107050)
        assert (not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
                and GetCurrentStateElapsedFrames() > 1)
        """State 60"""
        UnkUnlockDecal(6512)
    else:
        pass
    """State 57"""
    assert (not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            and GetCurrentStateElapsedFrames() > 1)
    """State 82"""
    return 0

def t001000000_x32():
    """State 0,1"""
    c1_230(0)
    """State 2,3"""
    # tutorial:2103020:Training Exercises Updated: TRAINING
    ShowTutorialMessage(2103020)
    # mission:9204:"Intermediate Support 3: Tetrapod ACs"
    SetMissionState(9204, 0, 1)
    # mission:9205:"Intermediate Support 4: Tank ACs"
    SetMissionState(9205, 0, 1)
    assert (not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            and GetCurrentStateElapsedFrames() > 1)
    """State 4"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    return 0

def t001000000_x33(text3=_, z3=_):
    """State 0,7"""
    assert t001000000_x0()
    """State 1"""
    ShowGrandioseTextPresentation(z3)
    assert GetCurrentStateElapsedTime() > 2
    """State 2,3"""
    TalkToPlayer(text3, -1, -1, 0)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 4"""
    c1_255()
    assert GetCurrentStateElapsedTime() > 2.3
    """State 6,5"""
    c1_229(7)
    assert f320(7) == 1
    """State 8"""
    return 0

def t001000000_x34():
    """State 0,1"""
    c1_230(0)
    c1_229(7)
    # eventflag:3136:	reserve 11 	予備11
    SetEventFlag(3136, 1)
    """State 2,3"""
    # tutorial:2104000:Access Granted: LOGHUNT
    ShowTutorialMessage(2104000)
    assert (not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            and GetCurrentStateElapsedFrames() > 1)
    """State 4"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    return 0

def t001000000_x35():
    """State 0,1"""
    c1_230(0)
    c1_229(7)
    # eventflag:3158:	Arena unlock progress 9 	アリーナ解禁進行度9
    SetEventFlag(3158, 1)
    """State 2,3"""
    # tutorial:2101040:Verification Data Updated: ARENA
    ShowTutorialMessage(2101040)
    assert (not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            and GetCurrentStateElapsedFrames() > 1)
    """State 4"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    return 0

def t001000000_x36():
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 1"""
    c1_230(0)
    """State 2,3"""
    # tutorial:2103020:Training Exercises Updated: TRAINING
    ShowTutorialMessage(2103020)
    # mission:9206:"Advanced Mercenary Certification"
    SetMissionState(9206, 0, 1)
    # eventflag:6438:	Tremo 7 released 	トレモ７出した
    SetEventFlag(6438, 1)
    assert (not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            and GetCurrentStateElapsedFrames() > 1)
    """State 4"""
    # eventflag:3200:	Menu non-display judgment 	メニュー非表示判定
    SetEventFlag(3200, 0)
    """State 5"""
    return 0

def t001000000_x37(text2=_, z2=_):
    """State 0,1"""
    c1_117(0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0)
    c1_238(0, 2, 800000090)
    assert GetCurrentStateElapsedTime() > 2 and f336() == 1
    """State 3"""
    StartEvent(0, 3705)
    """State 2"""
    c1_117(0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 5, 0)
    assert GetCurrentStateElapsedTime() > 4
    """State 11"""
    ShowGrandioseTextPresentation(z2)
    assert GetCurrentStateElapsedTime() > 2
    """State 10,9"""
    TalkToPlayer(text2, -1, -1, 0)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 8"""
    c1_255()
    c1_224(40001)
    if GetChapter() == 3:
        """State 17"""
        c1_224(50030)
    elif GetChapter() == 2:
        """State 16"""
        c1_224(40001)
    elif GetChapter() == 1:
        """State 15"""
        c1_224(50030)
    else:
        """State 14"""
        c1_224(40001)
    """State 18"""
    assert GetCurrentStateElapsedTime() > 2.5
    """State 6,7"""
    c1_229(7)
    """State 12,4"""
    c1_117(0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 4, 0)
    # eventflag:3920:	whispered flag 	ひそひそ話をしたフラグ
    SetEventFlag(3920, 1)
    assert f336() == 1
    """State 13"""
    StartEvent(0, 3706)
    assert GetCurrentStateElapsedTime() > 1
    """State 5"""
    c1_117(0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0.5, 0)
    assert f336() == 1
    """State 19"""
    return 0

def t001000000_x38():
    """State 0,1"""
    # mission:7900:"Destroy the Transport Helicopters", mission:7980:"Destroy the Tester AC", eventflag:3405:	[Garage] Judgment by seeing the story production_Chapter 1 progress 6 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度6
    if UnkMissionComplete(7900, 1) == 1 and UnkMissionComplete(7980, 1) == 1 and not GetEventFlag(3405):
        """State 2"""
        if UnkGameCycle() > 1:
            """State 4,13"""
            # talk:911010010:"Michigan, about leaving 621 with the Redguns..."
            assert t001000000_x37(text2=911010010, z2=91000200)
        else:
            """State 12"""
            # talk:911000010:"Well, well, well! Handler Walter!"
            assert t001000000_x37(text2=911000010, z2=91000200)
        """State 3"""
        # eventflag:3405:	[Garage] Judgment by seeing the story production_Chapter 1 progress 6 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度6
        SetEventFlag(3405, 1)
    else:
        """State 5"""
        # mission:2020:"Attack the Dam Complex", mission:2080:"Destroy the Weaponized Mining Ship", eventflag:3408:	[Garage] Judgment by seeing the story production_Chapter 1 progress 9 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度9
        if UnkMissionComplete(2020, 1) == 1 and UnkMissionComplete(2080, 1) == 1 and not GetEventFlag(3408):
            """State 6"""
            pass
        # mission:2025:"Attack the Dam Complex", mission:2080:"Destroy the Weaponized Mining Ship", eventflag:3408:	[Garage] Judgment by seeing the story production_Chapter 1 progress 9 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度9
        elif UnkMissionComplete(2025, 1) == 1 and UnkMissionComplete(2080, 1) == 1 and not GetEventFlag(3408):
            """State 7"""
            pass
        # mission:2025:"Attack the Dam Complex", mission:2250:"Escort the Weaponized Mining Ship", eventflag:3408:	[Garage] Judgment by seeing the story production_Chapter 1 progress 9 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度9
        elif UnkMissionComplete(2025, 1) == 1 and UnkMissionComplete(2250, 1) == 1 and not GetEventFlag(3408):
            """State 8,15"""
            # talk:912020010:"You must be the handler, I presume?\nFor the independent mercenary Raven."
            assert t001000000_x37(text2=912020010, z2=91000210)
            Goto('L1')
        else:
            """State 9"""
            # eventflag:3453:	[Garage] Judgment by seeing the story production_Chapter 1 progress 13 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度13, mission:2100:"Retrieve Combat Logs", mission:2060:"Investigate BAWS Arsenal No. 2"
            if (not GetEventFlag(3453) and UnkMissionComplete(2100, 1) == 1 and UnkMissionComplete(2060,
                1) == 1):
                """State 10"""
                Label('L0')
                # mission:2200:"Obstruct the Mandatory Inspection"
                if UnkMissionComplete(2200, 0) == 1:
                    """State 17"""
                    # talk:914020010:"Long time no see, Walter.\nLooking good for a change."
                    assert t001000000_x37(text2=914020010, z2=91000220)
                    Goto('L1')
                else:
                    """State 16"""
                    # talk:914000010:"Long time no see, Walter.\nLooking good for a change."
                    assert t001000000_x37(text2=914000010, z2=91000220)
                    Goto('L1')
            # eventflag:3453:	[Garage] Judgment by seeing the story production_Chapter 1 progress 13 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度13, mission:2140:"Prisoner Rescue", mission:2200:"Obstruct the Mandatory Inspection"
            elif (not GetEventFlag(3453) and UnkMissionComplete(2140, 1) == 1 and UnkMissionComplete(2200,
                  1) == 1):
                Goto('L0')
            # eventflag:3453:	[Garage] Judgment by seeing the story production_Chapter 1 progress 13 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度13, mission:2140:"Prisoner Rescue", mission:2200:"Obstruct the Mandatory Inspection"
            elif (not GetEventFlag(3453) and UnkMissionComplete(2140, 1) == 1 and UnkMissionComplete(2200,
                  1) == 1):
                Goto('L0')
            # mission:2200:"Obstruct the Mandatory Inspection", mission:2100:"Retrieve Combat Logs", eventflag:3453:	[Garage] Judgment by seeing the story production_Chapter 1 progress 13 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度13
            elif UnkMissionComplete(2200, 1) == 1 and UnkMissionComplete(2100, 1) == 1 and not GetEventFlag(3453):
                Goto('L0')
            # eventflag:3453:	[Garage] Judgment by seeing the story production_Chapter 1 progress 13 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度13, mission:2140:"Prisoner Rescue", mission:2060:"Investigate BAWS Arsenal No. 2"
            elif (not GetEventFlag(3453) and UnkMissionComplete(2140, 1) == 1 and UnkMissionComplete(2060,
                  1) == 1):
                Goto('L0')
            else:
                Goto('L1')
        """State 14"""
        # talk:912000010:"You must be the handler, I presume?\nFor the independent mercenary Raven."
        assert t001000000_x37(text2=912000010, z2=91000210)
        """State 11"""
    """State 18"""
    Label('L1')
    return 0

def t001000000_x39():
    """State 0,1,5"""
    Label('L0')
    return 0
    """Unused"""
    """State 2,3"""
    # talk:921000010:"Guess you noticed that job from Balam...\nand decided to take it."
    assert t001000000_x37(text2=921000010, z2=91000010)
    Goto('L0')
    """State 4"""
    # talk:921020010:"Guess you noticed that job from Balam...\nand decided to take it."
    assert t001000000_x37(text2=921020010, z2=91000010)
    Goto('L0')

def t001000000_x40():
    """State 0,1"""
    # mission:2170:"Eliminate V.VII", mission:3420:"Tunnel Sabotage", mission:3030:"Attack the Refueling Base", eventflag:3426:	[Garage] Judgment by watching the story production Chapter 3 progress level 7 	【ガレージ】ストーリー演出を見た判定チャプター3進行度7
    if (UnkMissionComplete(2170, 1) == 1 and UnkMissionComplete(3420, 1) == 1 and UnkMissionComplete(3030,
        1) == 1 and not GetEventFlag(3426)):
        """State 2"""
        Label('L0')
        """State 7"""
        # eventflag:3425:	[Garage] Judgment after seeing the story production Chapter 3 progress 6 	【ガレージ】ストーリー演出を見た判定チャプター3進行度6
        SetEventFlag(3425, 1)
        """State 9"""
        # talk:932000010:"How's it going, Walter?"
        assert t001000000_x37(text2=932000010, z2=91000220)
    # mission:2170:"Eliminate V.VII", mission:7910:"Prevent Corporate Salvage of New Tech", mission:3030:"Attack the Refueling Base", eventflag:3426:	[Garage] Judgment by watching the story production Chapter 3 progress level 7 	【ガレージ】ストーリー演出を見た判定チャプター3進行度7
    elif (UnkMissionComplete(2170, 1) == 1 and UnkMissionComplete(7910, 1) == 1 and UnkMissionComplete(3030,
          1) == 1 and not GetEventFlag(3426)):
        Goto('L0')
    else:
        """State 3"""
        # mission:5100:"Survey the Uninhabited Floating City", mission:7990:"Eliminate the Enforcement Squads", mission:2220:"Heavy Missile Launch Support", eventflag:3460:	[Garage] Judgment by watching the story production Chapter 3 progress level 11 	【ガレージ】ストーリー演出を見た判定チャプター3進行度11
        if (UnkMissionComplete(5100, 1) == 1 and UnkMissionComplete(7990, 1) == 1 and UnkMissionComplete(2220,
            1) == 1 and not GetEventFlag(3460)):
            """State 4"""
            Label('L1')
            """State 10"""
            # talk:933000010:"You again? I'm a busy man.\nFar too busy for the likes of you."
            assert t001000000_x37(text2=933000010, z2=91000210)
        # mission:5105:"Survey the Uninhabited Floating City", mission:2220:"Heavy Missile Launch Support", mission:7990:"Eliminate the Enforcement Squads", eventflag:3460:	[Garage] Judgment by watching the story production Chapter 3 progress level 11 	【ガレージ】ストーリー演出を見た判定チャプター3進行度11
        elif (UnkMissionComplete(5105, 1) == 1 and UnkMissionComplete(2220, 1) == 1 and UnkMissionComplete(7990,
              1) == 1 and not GetEventFlag(3460)):
            Goto('L1')
        # eventflag:3460:	[Garage] Judgment by watching the story production Chapter 3 progress level 11 	【ガレージ】ストーリー演出を見た判定チャプター3進行度11, mission:3430:"Destroy the Special Forces Craft", mission:5100:"Survey the Uninhabited Floating City", mission:2220:"Heavy Missile Launch Support"
        elif (not GetEventFlag(3460) and UnkMissionComplete(3430, 1) == 1 and UnkMissionComplete(5100,
              1) == 1 and UnkMissionComplete(2220, 1) == 1):
            Goto('L1')
        # eventflag:3460:	[Garage] Judgment by watching the story production Chapter 3 progress level 11 	【ガレージ】ストーリー演出を見た判定チャプター3進行度11, mission:2220:"Heavy Missile Launch Support", mission:5105:"Survey the Uninhabited Floating City", mission:3430:"Destroy the Special Forces Craft"
        elif (not GetEventFlag(3460) and UnkMissionComplete(2220, 1) == 1 and UnkMissionComplete(5105,
              1) == 1 and UnkMissionComplete(3430, 1) == 1):
            Goto('L1')
        else:
            """State 5"""
            # eventflag:3466:	[Garage] Judgment by seeing the story production Chapter 3 progress level 17 	【ガレージ】ストーリー演出を見た判定チャプター3進行度17, mission:2211:"Coral Export Denial", mission:2240:"Defend the Dam Complex", mission:3320:"Eliminate "Honest" Brute"
            if (not GetEventFlag(3466) and UnkMissionComplete(2211, 1) == 1 and UnkMissionComplete(2240,
                1) == 1 and UnkMissionComplete(3320, 1) == 1):
                """State 6"""
                Label('L2')
                """State 8"""
                # eventflag:3465:	[Garage] Judgment after seeing the story production Chapter 3 progress 16 	【ガレージ】ストーリー演出を見た判定チャプター3進行度16
                SetEventFlag(3465, 1)
                """State 11"""
                # talk:935000010:"We got ourselves a deal, Handler Walter!"
                assert t001000000_x37(text2=935000010, z2=91000200)
            # eventflag:3466:	[Garage] Judgment by seeing the story production Chapter 3 progress level 17 	【ガレージ】ストーリー演出を見た判定チャプター3進行度17, mission:3320:"Eliminate "Honest" Brute", mission:2240:"Defend the Dam Complex", mission:3500:"Historic Data Recovery"
            elif (not GetEventFlag(3466) and UnkMissionComplete(3320, 1) == 1 and UnkMissionComplete(2240,
                  1) == 1 and UnkMissionComplete(3500, 1) == 1):
                Goto('L2')
            # eventflag:3466:	[Garage] Judgment by seeing the story production Chapter 3 progress level 17 	【ガレージ】ストーリー演出を見た判定チャプター3進行度17, mission:2240:"Defend the Dam Complex", mission:3320:"Eliminate "Honest" Brute", mission:3500:"Historic Data Recovery"
            elif (not GetEventFlag(3466) and UnkMissionComplete(2240, 1) == 1 and UnkMissionComplete(3320,
                  1) == 1 and UnkMissionComplete(3500, 1) == 1):
                Goto('L2')
            # eventflag:3466:	[Garage] Judgment by seeing the story production Chapter 3 progress level 17 	【ガレージ】ストーリー演出を見た判定チャプター3進行度17, mission:3320:"Eliminate "Honest" Brute", mission:7950:"Defend the Old Spaceport", mission:3500:"Historic Data Recovery"
            elif (not GetEventFlag(3466) and UnkMissionComplete(3320, 1) == 1 and UnkMissionComplete(7950,
                  1) == 1 and UnkMissionComplete(3500, 1) == 1):
                Goto('L2')
            # mission:3320:"Eliminate "Honest" Brute", mission:7950:"Defend the Old Spaceport", mission:3500:"Historic Data Recovery", eventflag:3466:	[Garage] Judgment by seeing the story production Chapter 3 progress level 17 	【ガレージ】ストーリー演出を見た判定チャプター3進行度17
            elif (UnkMissionComplete(3320, 1) == 1 and UnkMissionComplete(7950, 1) == 1 and UnkMissionComplete(3500,
                  1) == 1 and not GetEventFlag(3466)):
                Goto('L2')
            # mission:7950:"Defend the Old Spaceport", mission:2211:"Coral Export Denial", mission:3320:"Eliminate "Honest" Brute", eventflag:3466:	[Garage] Judgment by seeing the story production Chapter 3 progress level 17 	【ガレージ】ストーリー演出を見た判定チャプター3進行度17
            elif (UnkMissionComplete(7950, 1) == 1 and UnkMissionComplete(2211, 1) == 1 and UnkMissionComplete(3320,
                  1) == 1 and not GetEventFlag(3466)):
                Goto('L2')
            else:
                pass
    """State 12"""
    return 0

def t001000000_x41():
    """State 0,1"""
    # eventflag:3433:	[Garage] Judgment by seeing the story production_Chapter 4 progress 4 	【ガレージ】ストーリー演出を見た判定_チャプター4進行度4, mission:4020:"Underground Exploration – Depth 3"
    if not GetEventFlag(3433) and UnkMissionComplete(4020, 1) == 1:
        """State 2,3"""
        # talk:943000010:"How was the trip underground, Walter?"
        assert t001000000_x37(text2=943000010, z2=91000220)
    else:
        pass
    """State 4"""
    return 0

def t001000000_x42():
    """State 0,1"""
    c1_230(0)
    c1_229(7)
    # eventflag:6015:	Arena unlocking progress 6 take over 	アリーナ解禁進行度6　引継ぎ
    SetEventFlag(6015, 1)
    """State 2,3"""
    # tutorial:2101040:Verification Data Updated: ARENA
    ShowTutorialMessage(2101040)
    assert (not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            and GetCurrentStateElapsedFrames() > 1)
    """State 4"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    return 0

def t001000000_x43():
    """State 0,1"""
    c1_230(0)
    c1_229(7)
    # eventflag:6016:	Arena unlocking progress 7 take over 	アリーナ解禁進行度7　引継ぎ
    SetEventFlag(6016, 1)
    """State 2,3"""
    # tutorial:2101040:Verification Data Updated: ARENA
    ShowTutorialMessage(2101040)
    assert (not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            and GetCurrentStateElapsedFrames() > 1)
    """State 4"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    return 0

def t001000000_x44():
    """State 0,1"""
    c1_230(0)
    c1_229(7)
    # eventflag:6017:	Arena unlocking progress level 8 takeover 	アリーナ解禁進行度8　引継ぎ
    SetEventFlag(6017, 1)
    # eventflag:6018:	let the air out even once 	一度でもエアを出した
    SetEventFlag(6018, 1)
    """State 2,3"""
    # tutorial:2101040:Verification Data Updated: ARENA
    ShowTutorialMessage(2101040)
    assert (not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            and GetCurrentStateElapsedFrames() > 1)
    """State 4"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    return 0

def t001000000_x45():
    """State 0,1"""
    c1_230(0)
    c1_229(7)
    """State 2,3"""
    # tutorial:2105000:Access Granted: AC DESIGN
    ShowTutorialMessage(2105000)
    assert (not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            and GetCurrentStateElapsedFrames() > 1)
    """State 4"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    return 0

def t001000000_x46(text1=_, z1=91000060):
    """State 0,7"""
    assert t001000000_x0()
    """State 1"""
    ShowGrandioseTextPresentation(z1)
    assert GetCurrentStateElapsedTime() > 2
    """State 2,3"""
    TalkToPlayer(text1, -1, -1, 0)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 4"""
    c1_255()
    assert GetCurrentStateElapsedTime() > 2.3
    """State 6,5"""
    c1_229(7)
    assert f320(7) == 1
    """State 8"""
    return 0

def t001000000_x47():
    """State 0,1"""
    # eventflag:3133:	ONLINE_Arena_Unlocking 	ONLINE_Arena_解禁用
    SetEventFlag(3133, 1)
    c1_230(0)
    """State 2,3"""
    # tutorial:2101020:Access Granted: NEST
    ShowTutorialMessage(2101020)
    assert (not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            and GetCurrentStateElapsedFrames() > 1)
    """State 4"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    return 0

def t001000000_x48():
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 1"""
    c1_230(0)
    c1_229(7)
    """State 2,3"""
    # tutorial:2106000:Prototype Issued: VE-60SNA
    ShowTutorialMessage(2106000)
    assert GetCurrentStateElapsedFrames() > 1
    """State 4"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    return 0

def t001000000_x49():
    """State 0,1"""
    # mission:7900:"Destroy the Transport Helicopters", mission:7980:"Destroy the Tester AC", eventflag:3405:	[Garage] Judgment by seeing the story production_Chapter 1 progress 6 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度6
    if UnkMissionComplete(7900, 1) == 1 and UnkMissionComplete(7980, 1) == 1 and not GetEventFlag(3405):
        """State 2"""
        Label('L0')
        c1_238(0, 2, 800000090)
    else:
        """State 3"""
        # mission:2020:"Attack the Dam Complex", mission:2080:"Destroy the Weaponized Mining Ship", eventflag:3408:	[Garage] Judgment by seeing the story production_Chapter 1 progress 9 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度9
        if UnkMissionComplete(2020, 1) == 1 and UnkMissionComplete(2080, 1) == 1 and not GetEventFlag(3408):
            """State 4"""
            Label('L1')
            Goto('L0')
        # mission:2025:"Attack the Dam Complex", mission:2080:"Destroy the Weaponized Mining Ship", eventflag:3408:	[Garage] Judgment by seeing the story production_Chapter 1 progress 9 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度9
        elif UnkMissionComplete(2025, 1) == 1 and UnkMissionComplete(2080, 1) == 1 and not GetEventFlag(3408):
            Goto('L1')
        # mission:2025:"Attack the Dam Complex", mission:2250:"Escort the Weaponized Mining Ship", eventflag:3408:	[Garage] Judgment by seeing the story production_Chapter 1 progress 9 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度9
        elif UnkMissionComplete(2025, 1) == 1 and UnkMissionComplete(2250, 1) == 1 and not GetEventFlag(3408):
            Goto('L1')
        else:
            """State 5"""
            # eventflag:3453:	[Garage] Judgment by seeing the story production_Chapter 1 progress 13 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度13, mission:2140:"Prisoner Rescue", mission:2200:"Obstruct the Mandatory Inspection"
            if (not GetEventFlag(3453) and UnkMissionComplete(2140, 1) == 1 and UnkMissionComplete(2200,
                1) == 1):
                """State 6"""
                Label('L2')
                Goto('L0')
            # eventflag:3453:	[Garage] Judgment by seeing the story production_Chapter 1 progress 13 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度13, mission:2100:"Retrieve Combat Logs", mission:2060:"Investigate BAWS Arsenal No. 2"
            elif (not GetEventFlag(3453) and UnkMissionComplete(2100, 1) == 1 and UnkMissionComplete(2060,
                  1) == 1):
                Goto('L2')
            # eventflag:3453:	[Garage] Judgment by seeing the story production_Chapter 1 progress 13 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度13, mission:2140:"Prisoner Rescue", mission:2200:"Obstruct the Mandatory Inspection"
            elif (not GetEventFlag(3453) and UnkMissionComplete(2140, 1) == 1 and UnkMissionComplete(2200,
                  1) == 1):
                Goto('L2')
            # mission:2200:"Obstruct the Mandatory Inspection", mission:2100:"Retrieve Combat Logs", eventflag:3453:	[Garage] Judgment by seeing the story production_Chapter 1 progress 13 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度13
            elif UnkMissionComplete(2200, 1) == 1 and UnkMissionComplete(2100, 1) == 1 and not GetEventFlag(3453):
                Goto('L2')
            # eventflag:3453:	[Garage] Judgment by seeing the story production_Chapter 1 progress 13 	【ガレージ】ストーリー演出を見た判定_チャプター1進行度13, mission:2140:"Prisoner Rescue", mission:2060:"Investigate BAWS Arsenal No. 2"
            elif (not GetEventFlag(3453) and UnkMissionComplete(2140, 1) == 1 and UnkMissionComplete(2060,
                  1) == 1):
                Goto('L2')
            else:
                """State 7"""
                # mission:2170:"Eliminate V.VII", mission:7910:"Prevent Corporate Salvage of New Tech", mission:3030:"Attack the Refueling Base", eventflag:3426:	[Garage] Judgment by watching the story production Chapter 3 progress level 7 	【ガレージ】ストーリー演出を見た判定チャプター3進行度7
                if (UnkMissionComplete(2170, 1) == 1 and UnkMissionComplete(7910, 1) == 1 and UnkMissionComplete(3030,
                    1) == 1 and not GetEventFlag(3426)):
                    """State 8"""
                    Label('L3')
                # mission:2170:"Eliminate V.VII", mission:3420:"Tunnel Sabotage", mission:3030:"Attack the Refueling Base", eventflag:3426:	[Garage] Judgment by watching the story production Chapter 3 progress level 7 	【ガレージ】ストーリー演出を見た判定チャプター3進行度7
                elif (UnkMissionComplete(2170, 1) == 1 and UnkMissionComplete(3420, 1) == 1 and UnkMissionComplete(3030,
                      1) == 1 and not GetEventFlag(3426)):
                    Goto('L3')
                else:
                    """State 10"""
                    # mission:5100:"Survey the Uninhabited Floating City", mission:7990:"Eliminate the Enforcement Squads", mission:2220:"Heavy Missile Launch Support", eventflag:3460:	[Garage] Judgment by watching the story production Chapter 3 progress level 11 	【ガレージ】ストーリー演出を見た判定チャプター3進行度11
                    if (UnkMissionComplete(5100, 1) == 1 and UnkMissionComplete(7990, 1) == 1 and UnkMissionComplete(2220,
                        1) == 1 and not GetEventFlag(3460)):
                        """State 11"""
                        Label('L4')
                    # mission:5105:"Survey the Uninhabited Floating City", mission:2220:"Heavy Missile Launch Support", mission:7990:"Eliminate the Enforcement Squads", eventflag:3460:	[Garage] Judgment by watching the story production Chapter 3 progress level 11 	【ガレージ】ストーリー演出を見た判定チャプター3進行度11
                    elif (UnkMissionComplete(5105, 1) == 1 and UnkMissionComplete(2220, 1) == 1 and UnkMissionComplete(7990,
                          1) == 1 and not GetEventFlag(3460)):
                        Goto('L4')
                    # eventflag:3460:	[Garage] Judgment by watching the story production Chapter 3 progress level 11 	【ガレージ】ストーリー演出を見た判定チャプター3進行度11, mission:3430:"Destroy the Special Forces Craft", mission:5100:"Survey the Uninhabited Floating City", mission:2220:"Heavy Missile Launch Support"
                    elif (not GetEventFlag(3460) and UnkMissionComplete(3430, 1) == 1 and UnkMissionComplete(5100,
                          1) == 1 and UnkMissionComplete(2220, 1) == 1):
                        Goto('L4')
                    # eventflag:3460:	[Garage] Judgment by watching the story production Chapter 3 progress level 11 	【ガレージ】ストーリー演出を見た判定チャプター3進行度11, mission:2220:"Heavy Missile Launch Support", mission:5105:"Survey the Uninhabited Floating City", mission:3430:"Destroy the Special Forces Craft"
                    elif (not GetEventFlag(3460) and UnkMissionComplete(2220, 1) == 1 and UnkMissionComplete(5105,
                          1) == 1 and UnkMissionComplete(3430, 1) == 1):
                        Goto('L4')
                    else:
                        """State 13"""
                        # eventflag:3466:	[Garage] Judgment by seeing the story production Chapter 3 progress level 17 	【ガレージ】ストーリー演出を見た判定チャプター3進行度17, mission:2211:"Coral Export Denial", mission:2240:"Defend the Dam Complex", mission:3320:"Eliminate "Honest" Brute"
                        if (not GetEventFlag(3466) and UnkMissionComplete(2211, 1) == 1 and UnkMissionComplete(2240,
                            1) == 1 and UnkMissionComplete(3320, 1) == 1):
                            """State 12"""
                            Label('L5')
                        # eventflag:3466:	[Garage] Judgment by seeing the story production Chapter 3 progress level 17 	【ガレージ】ストーリー演出を見た判定チャプター3進行度17, mission:3320:"Eliminate "Honest" Brute", mission:2240:"Defend the Dam Complex", mission:3500:"Historic Data Recovery"
                        elif (not GetEventFlag(3466) and UnkMissionComplete(3320, 1) == 1 and UnkMissionComplete(2240,
                              1) == 1 and UnkMissionComplete(3500, 1) == 1):
                            Goto('L5')
                        # eventflag:3466:	[Garage] Judgment by seeing the story production Chapter 3 progress level 17 	【ガレージ】ストーリー演出を見た判定チャプター3進行度17, mission:2240:"Defend the Dam Complex", mission:3320:"Eliminate "Honest" Brute", mission:3500:"Historic Data Recovery"
                        elif (not GetEventFlag(3466) and UnkMissionComplete(2240, 1) == 1 and UnkMissionComplete(3320,
                              1) == 1 and UnkMissionComplete(3500, 1) == 1):
                            Goto('L5')
                        # eventflag:3466:	[Garage] Judgment by seeing the story production Chapter 3 progress level 17 	【ガレージ】ストーリー演出を見た判定チャプター3進行度17, mission:3320:"Eliminate "Honest" Brute", mission:7950:"Defend the Old Spaceport", mission:3500:"Historic Data Recovery"
                        elif (not GetEventFlag(3466) and UnkMissionComplete(3320, 1) == 1 and UnkMissionComplete(7950,
                              1) == 1 and UnkMissionComplete(3500, 1) == 1):
                            Goto('L5')
                        # mission:3320:"Eliminate "Honest" Brute", mission:7950:"Defend the Old Spaceport", mission:3500:"Historic Data Recovery", eventflag:3466:	[Garage] Judgment by seeing the story production Chapter 3 progress level 17 	【ガレージ】ストーリー演出を見た判定チャプター3進行度17
                        elif (UnkMissionComplete(3320, 1) == 1 and UnkMissionComplete(7950, 1) == 1 and
                              UnkMissionComplete(3500, 1) == 1 and not GetEventFlag(3466)):
                            Goto('L5')
                        # mission:7950:"Defend the Old Spaceport", mission:2211:"Coral Export Denial", mission:3320:"Eliminate "Honest" Brute", eventflag:3466:	[Garage] Judgment by seeing the story production Chapter 3 progress level 17 	【ガレージ】ストーリー演出を見た判定チャプター3進行度17
                        elif (UnkMissionComplete(7950, 1) == 1 and UnkMissionComplete(2211, 1) == 1 and
                              UnkMissionComplete(3320, 1) == 1 and not GetEventFlag(3466)):
                            Goto('L5')
                        else:
                            """State 15"""
                            # eventflag:3433:	[Garage] Judgment by seeing the story production_Chapter 4 progress 4 	【ガレージ】ストーリー演出を見た判定_チャプター4進行度4, mission:4020:"Underground Exploration – Depth 3"
                            if not GetEventFlag(3433) and UnkMissionComplete(4020, 1) == 1:
                                """State 14"""
                                c1_238(0, 2, 800000090)
                                Goto('L6')
                            else:
                                """State 16"""
                                return 0
                """State 9"""
                c1_238(0, 2, 800000090)
    """State 17"""
    Label('L6')
    return 1

def t001000000_x50():
    """State 0,1"""
    SetEventFlag(6245, 1)
    c1_230(0)
    c1_229(7)
    """State 2,3"""
    # tutorial:2100010:Products Updated: PARTS SHOP
    ShowTutorialMessage(2100010)
    assert (not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            and GetCurrentStateElapsedFrames() > 1)
    """State 4"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    return 0

