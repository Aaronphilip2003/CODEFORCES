import java.io.*;
public class Hulk_705A 
{
	public static void main(String args[])throws IOException
	{
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		int a=0;
		a=Integer.parseInt(br.readLine());
		 for (int i = 0; i < a; i++)
		 {
		        if (i % 2 == 0)
		        {
		            System.out.print( "I hate ");
		        } 
		        else
		        {
		            System.out.print( "I love ");
		        }
		        if (i != a - 1) 
		        {
		            System.out.print( "that ");
		        } else 
		        {
		            System.out.print( "it ");
		        }
		    }
		
		
	}

}
