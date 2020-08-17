public static void main(String args[])
	{
		//ListIterator<String> list_Iter = null;
		// Creating object of class linked list
		LinkedList<Integer> object = new LinkedList<Integer>();

		// Adding elements to the linked list
		object.add(1);
		object.add(3);
		object.addFirst(0);
		object.add(5);
		object.add(6);
		object.add(2);
		object.addLast(4);

		System.out.println("Linked list : " + object);  ;

		object.size();
		System.out.println("The Linked List has " +object.size() + " elements");

		System.out.println("\n LinkedList after sorting: ");
	}
}
 //Making an iterator
		list_Iter = object.listIterator();

		// Iterating through the created list from the position
		System.out.println("The list is as follows:");
		while(list_Iter.hasNext()){

		// Removing elements from the linked list
		object.remove("0");
		object.remove(3);
		object.removeFirst();
		object.removeLast();
		System.out.println("Linked list after deletion: " + object);

		// Finding elements in the linked list
		boolean status = object.contains("3");

		if(status)
			System.out.println("List contains the element '3' ");
		else
			System.out.println("List doesn't contain the element '3'");

		// Number of elements in the linked list
		int size = object.size();
		System.out.println("Size of linked list = " + size);

		// Get and set elements from linked list
		Object element = object.get(2);
		System.out.println("Element returned by get() : " + element);
		object.set(2, "Y");
		System.out.println("Linked list after change : " + object); 
