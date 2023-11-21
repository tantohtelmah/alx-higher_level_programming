#include <stdio.h>
#include <Python.h>

/**
* print_python_list - lists
* @p: pyobject
* Return: void
*/
void print_python_list(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);

	printf("List size: %zd\n", size);
}

/**
* print_python_bytes - lists
* @p: pyobject
* Return: void
*/
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size = PyBytes_Size(p);

	printf("Bytes size: %zd\n", size);
}

/**
*print_python_float - lists
* @p: pyobject
* Return: void
*/
void print_python_float(PyObject *p)
{
	double value = PyFloat_AsDouble(p);

	printf("Float value: %f\n", value);
}
