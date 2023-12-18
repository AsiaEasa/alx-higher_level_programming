#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - gives data of the PyListObject
 * @p: the PyObject
 */

void print_python_list(PyObject *p)
{
	PyObject *i_t;
	Py_ssize_t buff = 0;
	int i = 0;

	fflush(stdout);
	printf("[*] Python list info\n");
	if (PyList_CheckExact(p))
	{
		buff = PyList_GET_SIZE(p);
		printf("[*] Size of the Python List = %zd\n", buff);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
		while (i < buff)
		{
			i_t = PyList_GET_ITEM(p, i);
			printf("Element %d: %s\n", i, i_t->ob_type->tp_name);
			if (PyBytes_Check(i_t))
				print_python_bytes(i_t);
			else if (PyFloat_Check(i_t))
				print_python_float(i_t);
			i++;
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}

/**
 * print_python_float - gives data of the PyFloatObject
 * @p: the PyObject
 */
void print_python_float(PyObject *p)
{
	double num = 0;
	char *s = NULL;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	num = ((PyFloatObject *)p)->ob_fval;
	s = PyOS_double_to_string(num, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", s);
}

/**
 * print_python_bytes - gives data of the PyBytesObject
 * @p: the PyObject
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t buff = 0;
	Py_ssize_t i = 0;
	char *s = NULL;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	buff = PyBytes_Size(p);
	printf("  size: %zd\n", buff);
	s = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));
	printf("  trying string: %s\n", s);
	printf("  first %zd bytes:", buff < 10 ? buff + 1 : 10);
	while (i < buff + 1 && i < 10)
	{
		printf(" %02hhx", s[i]);
		i++;
	}
	printf("\n");
}
