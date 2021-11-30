import java.io.*;
public class Elephant_617A 
{
	public static void main(String args[])throws IOException
	{
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		int pos=0;
		pos=Integer.parseInt(br.readLine());
		if(pos%5==0)
		{
			System.out.println((pos/5));
		}
		else
		{
			System.out.println((pos/5)+1);
		}
	}

}
// 800 rated
