import java.util.*;
import java.io.*;
public class Bit_plus_plus_282A
{
	public static void main(String args[])throws IOException
	{
		Scanner sc=new Scanner(System.in);
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));		
		int operations=0;
		int count=0;
		String statement="";
		operations=Integer.parseInt(br.readLine());
		while(operations!=0)
		{
			statement=br.readLine();
			if(statement.equalsIgnoreCase("X++")||statement.equalsIgnoreCase("++X"))
			{
				count++;
			}
			else if(statement.equalsIgnoreCase("X--")||statement.equalsIgnoreCase("--X"))				
			{
				count--;
			}
			operations--;
		}
		System.out.println(count);
	}

}

// 800 rated program
