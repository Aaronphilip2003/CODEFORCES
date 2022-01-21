import java.io.*;
public class Stones_On_The_Table_266A
{
	public static void main(String args[])throws IOException
	{
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		int n=0;
		n=Integer.parseInt(br.readLine());
		String s="";
		s=br.readLine();
		int count=0;
		for(int i=0,j=1;i<n&&j<n;i++,j++)
		{
			char ch=s.charAt(i);
			char ch1=s.charAt(j);
			if(ch==ch1)
				count++;
		}
		System.out.println(count);
		
	}

}

// 800 rated program
