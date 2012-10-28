/*
 * Author: Zhihua Lai
 * Version: 0.1
 * BrainFuck Interpreter
 * 
*/
using System;
using System.IO;

namespace BrainFuck
{
    class BrainFuckInterpreter
    {
        private static string VER = "0.0.0.1";
        private static readonly int BUFSIZE = 65535;
        private int[] buf = new int[BUFSIZE];
        private int ptr { get; set; }
        private bool echo { get; set; }

        public BrainFuckInterpreter()
        {
            this.ptr = 0;
            this.Reset();
        }

        public static void PrintHelp()
        {
            Console.WriteLine("BrainFuck Interpreter " + VER);
            Console.WriteLine("http://www.zhihua-lai.com/acm");
            Console.WriteLine("Parameter: -h: Print Help");
            Console.WriteLine("Parameter: -e: Enable Echo Input Text");
            Console.WriteLine("Parameter: -d: Disable Echo Input Text");
            Console.WriteLine("Parameter: -p: Enable Keyboard Input");
            Console.WriteLine("Parameter: -v: Print Version");
            Console.WriteLine("Parameter: FileName");
        }

        public void Reset()
        {
            Array.Clear(this.buf, 0, this.buf.Length);
        }

        public void Interpret(string s)
        {
            int i = 0;
            int right = s.Length;
            while (i < right)
            {
                switch (s[i])
                {
                    case '>':
                        {
                            this.ptr++;
                            if (this.ptr >= BUFSIZE)
                            {
                                this.ptr = 0;
                            }
                            break;
                        }
                    case '<':
                        {
                            this.ptr--;
                            if (this.ptr < 0)
                            {
                                this.ptr = BUFSIZE - 1;
                            }
                            break;
                        }
                    case '.':
                        {
                            Console.Write((char)this.buf[this.ptr]);
                            break;
                        }
                    case '+':
                        {
                            this.buf[this.ptr]++;
                            break;
                        }
                    case '-':
                        {
                            this.buf[this.ptr]--;
                            break;
                        }
                    case '[':
                        {
                            if (this.buf[this.ptr] == 0)
                            {
                                int loop = 1;
                                while (loop > 0)
                                {
                                    i ++;
                                    char c = s[i];
                                    if (c == '[')
                                    {
                                        loop ++;
                                    }
                                    else
                                    if (c == ']')
                                    {
                                        loop --;
                                    }
                                }
                            }
                            break;
                        }
                    case ']':
                        {
                            int loop = 1;
                            while (loop > 0)
                            {
                                i --;
                                char c = s[i];
                                if (c == '[')
                                {
                                    loop --;
                                }
                                else
                                if (c == ']')
                                {
                                    loop ++;
                                }
                            }
                            i --;
                            break;
                        }
                    case ',':
                        {
                            // read a key
                            ConsoleKeyInfo key = Console.ReadKey(this.echo);
                            this.buf[this.ptr] = (int)key.KeyChar;
                            break;
                        }
                }
                i++; 
            }
        }

        static void Main(string[] args)
        {
            if (args.Length == 0)
            {
                Console.WriteLine("Try -h, Thanks!");
            }
            else
            {
                BrainFuckInterpreter bf = new BrainFuckInterpreter();
                foreach (string s in args)
                {
                    if (s[0] == '-') // switch options
                    {
                        for (int i = 1; i < s.Length; i++)
                        {
                            switch (s[i])
                            {
                                case 'h':
                                    {
                                        PrintHelp();
                                        break;
                                    }
                                case 'd':
                                    {
                                        bf.echo = false;
                                        break;
                                    }
                                case 'v':
                                    {
                                        Console.WriteLine(VER);
                                        break;
                                    }
                                case 'e':
                                    {
                                        bf.echo = true;
                                        break;
                                    }
                                case 'p':
                                    {
                                        string src = Console.In.ReadToEnd();
                                        bf.Interpret(src);
                                        break;
                                    }
                            }
                        }
                    }
                    else
                    {
                        if (File.Exists(s))
                        {
                            bf.Interpret(File.ReadAllText(s));
                        }
                        else
                        {
                            Console.WriteLine("File Open Error: " + s);
                        }
                    }
                }
            }
        }
    }
}
