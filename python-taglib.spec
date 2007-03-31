Summary:	Python bindings for TagLib
Name:		python-taglib
Version:	1.3.3
Release:	1emh
URL:		http://namingmuse.berlios.de
Source0:	http://download.berlios.de/namingmuse/%{name}-%{version}.tar.gz
# Source0-md5:	744882d6de33d13b9d80a238f3dc16ed
License:	GPL
Group:		Development/Libraries
BuildRequires:	python-devel
BuildRequires:	taglib-devel
BuildRequires:	swig-python
Requires:	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python bindings for TagLib, the audio meta data library for
mp3/ogg/flac/mpc/ape.

%prep
%setup -q

%build
%configure \
	 \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc
%{_libdir}/libpython_taglib.so
%{_libdir}/libpython_taglib.la
%{python_sitedir}/_TagLib.so
%{python_sitedir}/TagLib.*
