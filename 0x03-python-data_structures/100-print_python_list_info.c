#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int p_size, alloc, i;
	PyObject *o;

	p_size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", p_size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < p_size; i++)
	{
		printf("Element %d: ", i);

		o = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(o)->tp_name);
	}
}
