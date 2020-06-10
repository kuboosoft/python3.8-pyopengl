%global srcname PyOpenGL
%global shortname pyopengl

%undefine _debugsource_packages

Name:           python3.8-pyopengl
Version:        3.1.5
Release:        1%{?dist}
Summary:        Python bindings for OpenGL
License:        BSD
URL:            https://github.com/mcfletch/pyopengl
Source0:        https://pypi.python.org/packages/source/P/PyOpenGL/PyOpenGL-%{version}.tar.gz

%description
PyOpenGL is the cross platform Python binding to OpenGL and related APIs. It
includes support for OpenGL v1.1, GLU, GLUT v3.7, GLE 3 and WGL 4. It also
includes support for dozens of extensions (where supported in the underlying
implementation).

PyOpenGL is inter-operable with a large number of external GUI libraries
for Python including (Tkinter, wxPython, FxPy, PyGame, and Qt). 

BuildRequires:  gcc
BuildRequires:  python3.8-devel

BuildRequires:  python3.8-numpy
BuildRequires:  python3.8-Cython
Requires:       freeglut
Requires:       python3.8-numpy
Requires:       python3-tkinter


%prep
%autosetup -n PyOpenGL-%{version}

%build
    # Fix the shebang
    sed -i 's|#!/usr/bin/env python|#!/usr/bin/python3.8|'  OpenGL/Tk/__init__.py
        
    sed -i 's|#! /usr/bin/env python|#!/usr/bin/python3.8|' OpenGL/arrays/{_,}buffers.py

%install

/usr/bin/python3.8 setup.py install --root=%{buildroot} --optimize=1


# Remove shebangs - note that weirdly these files have a space between
# the #! and the /, so this sed recipe is not the usual one
pushd %{buildroot}/usr/lib/python3.8/site-packages/OpenGL/arrays
sed -i -e '/^#! \//, 1d' buffers.py _buffers.py
popd


%files
/usr/lib/python3.8/site-packages/%{srcname}-%{version}-py3.8.egg-info
/usr/lib/python3.8/site-packages/OpenGL/


%changelog
