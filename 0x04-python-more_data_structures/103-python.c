#include <Python.h>
#include <Python.h>

#include <object.h>

#include <listobject.h>

#include <bytesobject.h>


void print_python_bytes(PyObject *p)

{

        long int size;

        int i;

        char *trying_str = NULL;


        printf("[.] bytes object info\n");

        if (!PyBytes_Check(p))

        {

                printf("  [ERROR] Invalid Bytes Object\n");

                return;

        }


        PyBytes_AsStringAndSize(p, &trying_str, &size);


        printf("  size: %li\n", size);

        printf("  trying string: %s\n", trying_str);

        if (size < 10)

                printf("  first %li bytes:", size + 1);

        else

                printf("  first 10 bytes:");

        for (i = 0; i <= size && i < 10; i++)

                printf(" %02hhx", trying_str[i]);

        printf("\n");

}

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list(PyObject *p)
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
