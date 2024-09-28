using SoulsFormats;
using System;

namespace AC6_Roguelike
{
    public class EMEVD_Edits
    {
        public static void EditEMEVD()
        {
            Console.WriteLine("Editing EMEVDs...");

            var evd = EMEVD.Read($@"{Paths.GAME_PATH}\event\common.emevd.dcx");

            #region    DETECT PLAYER DEATH
            evd.Events.Find(e => e.ID == 0)
                .Instructions.Insert(0, new(2000, 0, [0, 10000, 0]));
            evd.Events.Add(new(10000)
            {
                Instructions = [
                    new(3, 0, [(sbyte)1, (byte)0, (byte)0, 9998]),              // trigger if flag 9998 is 0
                    new(4, 15, [(sbyte)2, 20000, (byte)0, 0, (sbyte)0, 1]),     // trigger if player died
                    new(0, 0, [(sbyte)1, (byte)1, (sbyte)2]),                   // trigger if 1st and 2nd conditions are true
                    new(0, 0, [(sbyte)0, (byte)1, (sbyte)1]),                   // trigger if 3rd condition is true
                    new(2003, 66, [(byte)0, 9998, (byte)1]),                    // sets flag 9998 to 1
                    new(2003, 24, [(byte)3, 20000000, 1 ]),                     // remove the 'Player Died' good
                    //new(2007, 2, (byte[])[33]),                                 // display 'ALL TARGETS DESTROYED' banner
                    new(1000, 4, (byte[])[1]),                                  // end flow
                ]
            });
            #endregion

            #region     RESET JAILBREAK
            evd.Events.Find(e => e.ID == 0)
                .Instructions.Insert(0, new(2000, 0, [0, 10001, 0]));

            evd.Events.Add(new(10001)
            {
                Instructions = [
                    new(3, 0, [(sbyte)1, (byte)1, (byte)0, 9900]),              // trigger if flag 9900 is 1
                    new(3, 4, [(sbyte)2, (byte)3, 20000000, (byte)0]),          // IfPlayer(1: Has / 0: Doesn't Have)Item the 'Player Died' good
                    new(0, 0, [(sbyte)1, (byte)1, (sbyte)2]),                   // trigger if 1st and 2nd conditions are true
                    new(0, 0, [(sbyte)0, (byte)1, (sbyte)1]),                   // trigger if 3rd condition is true
                    new(2004, 52, [30000020]),                                  // ChangeCharacter -> reset to JAILBREAK
                    new(2003, 66, [(byte)0, 9999, (byte)1]),                    // sets flag 9999 to 1
                    new(1000, 4, (byte[])[1]),                                  // end flow
                ]
            });
            #endregion


            evd.Write($@"{Paths.MOD_PATH}\event\common.emevd.dcx");

            Console.WriteLine("EMEVDs edited.");
        }
    }
}
