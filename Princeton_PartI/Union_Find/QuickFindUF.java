public class QuickFindUF{
	private int[] id;

	/*Constructor*/
	public QuickFindUF(int N){
		id = new int[N];
		for (int i = 0; i < N; i++)
			id[i] = i;
	}

	/*
	  test if two points are connected
	  input: the indices of two points
	  ouput: true if two points are connected
	  logic: if two points have the same id value they are connected
	*/
	public boolean connected(int p, int q){
		return id[p] == id[q];
	}

	/*
	  connect two points
	  input: the indices of two points
	  output: nothing
	  logic: change all entries whose id equals to id[p] to id[q]
	  	so that we know thay are all connected now
	*/
	public void union(int p, int q){
		int pid = id[p];
		int qid = id[q];
		for (int i = 0; i < id.length; i++)
			if (id[i] == pid) id[i] = qid;
	}
}