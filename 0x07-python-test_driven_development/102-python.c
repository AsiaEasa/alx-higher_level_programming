#include <stdio.h>
#include <stdlib.h>
#include <wchar.h>
#include <Python.h>
#include <unicodeobject.h>

/**
 * display_python_string_info - prints information about Python strings
 * @python_str: address of PyObject struct
 */
void display_python_string_info(PyObject *python_str)
{
    printf("[.] String object details\n");
    if (strcmp(python_str->ob_type->tp_name, "str"))
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }
    if (PyUnicode_IS_COMPACT_ASCII(python_str))
        printf("  Type: Compact ASCII\n");
    else
        printf("  Type: Compact Unicode Object\n");
    printf("  Length: %lu\n", PyUnicode_GET_LENGTH(python_str));
    printf("  Value: %ls\n", PyUnicode_AS_UNICODE(python_str));
}
