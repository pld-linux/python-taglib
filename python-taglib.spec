Summary:	Python bindings for TagLib
Summary(pl.UTF-8):	Wiązania Pythona dla biblioteki TagLib
Name:		python-taglib
Version:	1.3.3
Release:	1
License:	GPL
Group:		Libraries/Python
Source0:	http://download.berlios.de/namingmuse/%{name}-%{version}.tar.gz
# Source0-md5:	ede76df44e0a82a64a0855f99e0cb4df
URL:		http://namingmuse.berlios.de/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	swig-python
BuildRequires:	taglib-devel
%pyrequires_eq	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python bindings for TagLib, the audio meta data library for
mp3/ogg/flac/mpc/ape.

%description -l pl.UTF-8
Wiązania Pythona dla biblioteki TagLib obsługującej metadane dla
plików mp3/ogg/flac/mpc/ape.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpython_taglib.so
# not needed?
%{_libdir}/libpython_taglib.la
%attr(755,root,root) %{py_sitedir}/_TagLib.so
# py[co]?
%{py_sitedir}/TagLib.*
