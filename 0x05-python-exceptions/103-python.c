#include <Python.h>

#include <floatobject.h>

#include <object.h>

#include <listobject.h>

#include <bytesobject.h>

void print_python_float(PyObject *p)
{
	double N;
	setbuf(stdout, NULL);
	printf("[.] float object info\n");
	if(strcmp(p->op_type->tp_name, "float"))
		{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	N = ((PyFloatObject *)p)->ob_fval;
	printf("  value: %s\n", PyOS_double_to_string(N, 'r', 0, PY_DTSF_ADD_DOT_O, NULL));
}
void print_python_bytes(PyObject *p)

{

	long int size;

	int i;

	char *_str = NULL;


	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	PyBytes_AsStringAndSize(p, &_str, &size);


	printf("  size: %li\n", size);

	printf("  trying string: %s\n", _str);

	if (size < 10)

		printf("  first %li bytes:", size + 1);

	else

		printf("  first 10 bytes:");

	for (i = 0; i <= size && i < 10; i++)

		printf(" %02hhx", _str[i]);

	printf("\n");

}


void print_python_list(PyObject *p)

{

	long int size = PyList_Size(p);

	int i;

	PyListObject *list = (PyListObject *)p;

	const char *type;

	printf("[*] Python list info\n");

	printf("[*] Size of the Python List = %li\n", size);

	printf("[*] Allocated = %li\n", list->allocated);

	for (i = 0; i < size; i++)

	{

		type = (list->ob_item[i])->ob_type->tp_name;

		printf("Element %i: %s\n", i, type);

		if (!strcmp(type, "bytes"))

			print_python_bytes(list->ob_item[i]);
		else if (strcmp(type, "float") == 0)
			print_python_float(list->ob_item[i]);
	}}
