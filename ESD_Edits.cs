using System;
namespace AC6_Roguelike
{
    public class ESD_Edits
    {
        public static void EditESD()
        {
            Console.WriteLine("Editing ESDs...");

            string py_file = $@".\esd_py\t001000000.py";

            string[] compile_args = {
                "-ac6",
                "-basedir", $@"{Paths.GAME_PATH}",
                "-i", @$"{Paths.GIT_PATH}AC6-Roguelike\esd_py\t001000000.py",
                "-writebnd", $@"{Paths.MOD_PATH}\script\talk"
            };

            string[] decompile_args = {
                "-ac6",
                "-basedir", $@"{Paths.GAME_PATH}",
                "-writepy", @$"{Paths.GIT_PATH}AC6-Roguelike\esd_dumps_py\%m.py"
            };

            string[] decompile_debug = {
                "-ac6",
                "-basedir", $@"{Paths.GAME_PATH}",
                "-i",  $@"{Paths.MOD_PATH}\script\talk\m00_00_00_00.talkesdbnd.dcx",
                "-f", "t001000000",
                "-writepy", @$"{Paths.GIT_PATH}AC6-Roguelike\esd_dumps_py\%e.py"
            };

            Console.WriteLine("Running ESDLang...");
            foreach (string arg in compile_args)
            {
                Console.Write(arg + " ");
            }

            Console.WriteLine("Writing Custom ESD to game");
            ESDLang.Script.Program.Main(compile_args);

            Console.WriteLine("Decompiling ESDs...");
            ESDLang.Script.Program.Main(decompile_debug);

            Console.WriteLine("Done!");
        }
    }
}
