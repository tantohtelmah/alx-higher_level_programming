#include <Python.h>
#include <stdio.h>

void print_python_string(PyObject *p)
{
    Py_ssize_t len;
    wchar_t *str;

    printf("[.] string object info\n");
    if (!PyUnicode_Check(p))
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }
    len = PyUnicode_GetLength(p);
    str = PyUnicode_AsWideCharString(p, &len);
    printf("  type: %s\n", Py_TYPE(p)->tp_name);
    printf("  length: %ld\n", len);
    printf("  value: %ls\n", str);
    PyMem_Free(str);
}
