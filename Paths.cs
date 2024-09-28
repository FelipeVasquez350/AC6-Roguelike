using System;
using System.Collections.Generic;
using System.IO;
using System.Text;

namespace AC6_Roguelike
{
    public class Paths
    {
        public static string GIT_PATH = Path.GetFullPath(Path.Combine(AppContext.BaseDirectory, @"..\..\..\..\"));
        public static string GAME_PATH = @"D:\SteamLibrary\steamapps\common\MODDED ARMORED CORE VI FIRES OF RUBICON\Game";
        public static string MOD_PATH = @$"{GIT_PATH}AC6-Roguelike\mod";
        public static string DIST_PATH = @$"{GIT_PATH}ESDLang\dist";
    }
}
