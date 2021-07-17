import java.io.*;
import java.util.*;
public class Bor_or_girl_236A
{
	public static void main(String args[])throws IOException
	{
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		String s="";		
		s=br.readLine();
		char[] ch=new char[s.length()];
		for(int i=0;i<s.length();i++)
		{
			ch[i]=s.charAt(i);
		}
		
		String newWord="";
		
		for(int i=0;i<ch.length;i++)
		{
			if(newWord.indexOf(ch[i])==-1)// check if a char already exist, if not exist then return -1		
			{
				newWord+=ch[i];
			}
		}
		int length=newWord.length();
		if(length%2==0)
		{
			System.out.println("CHAT WITH HER!");
		}
		else
		{
			System.out.println("IGNORE HIM!");
		}
		
		
	}

}
