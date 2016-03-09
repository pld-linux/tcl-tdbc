Summary:	TDBC - Tcl Database Connectivity
Summary(pl.UTF-8):	TDBC - Tcl Database Connectivity (łączność Tcl z bazami danych)
Name:		tcl-tdbc
Version:	1.0.4
Release:	1
License:	Tcl (BSD-like)
Group:		Libraries
Source0:	http://downloads.sourceforge.net/tcl/tdbc%{version}.tar.gz
# Source0-md5:	5b88b4f2ed851b97bc4c391203788c09
URL:		http://tdbc.tcl.tk/
BuildRequires:	sed >= 4.0
BuildRequires:	tcl-devel >= 8.5
Requires:	tcl >= 8.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TDBC Tcl module contains the base classes and SQL tokenizer of Tcl
Database Connectivity. To access databases, you also need one or more
driver modules for the database manager(s) from tcl-tdbc-* packages.

%description -l pl.UTF-8
Moduł Tcl TDBC zawiera klasy bazowe oraz tokenizer SQL będące częścią
szkieletu Tcl Database Connectivity. W celu dostępu do baz danych
potrzebne są jeszcze moduły sterowników do odpowiednich silników baz
danych z pakietów tcl-tdbc-*.

%package devel
Summary:	Development files for Tcl TDBC module
Summary(pl.UTF-8):	Pliki programistyczna modułu Tcl TDBC
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	tcl-devel >= 8.5

%description devel
Development files for Tcl TDBC module.

%description devel -l pl.UTF-8
Pliki programistyczna modułu Tcl TDBC.

%prep
%setup -q -n tdbc%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# allow dependency generation
chmod 755 $RPM_BUILD_ROOT%{_libdir}/tdbc%{version}/*.so

# hide build paths
%{__sed} -e '/^[Tt][Dd][Bb][Cc]_BUILD_STUB_LIB_SPEC/s,-L.* -l,-L%{_libdir}/tdbc%{version} -l,' \
	-e '/^[Tt][Dd][Bb][Cc]_BUILD_STUB_LIB_PATH/s,=".*libtdbcstub,="%{_libdir}/tdbc%{version}/libtdbcstub,' \
	-e '/^[Tt][Dd][Bb][Cc]_SRC_DIR/s,=".*",="%{_libdir}/tdbc%{version}",' \
	-e '/^[Tt][Dd][Bb][Cc]_BUILD_INCLUDE_SPEC/s,"-I.*","-I%{_includedir}",' \
	-e '/^[Tt][Dd][Bb][Cc]_LIBRARY_PATH/s,=".*",="%{_libdir}/tdbc%{version}",' \
	-e '/^[Tt][Dd][Bb][Cc]_BUILD_LIBRARY_PATH/s,=".*",="%{_libdir}/tdbc%{version}",' \
	-i $RPM_BUILD_ROOT%{_libdir}/tdbc%{version}/tdbcConfig.sh

# tdbc drivers look here for tdbc configuration
%{__mv} $RPM_BUILD_ROOT%{_libdir}/tdbc%{version}/tdbcConfig.sh $RPM_BUILD_ROOT%{_prefix}/lib

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README license.terms
%dir %{_libdir}/tdbc%{version}
%attr(755,root,root) %{_libdir}/tdbc%{version}/libtdbc%{version}.so
%{_libdir}/tdbc%{version}/*.tcl
%{_includedir}/tdbc.h
%{_includedir}/tdbcDecls.h
%{_includedir}/tdbcInt.h
%{_mandir}/mann/tdbc*.n*

%files devel
%defattr(644,root,root,755)
%{_libdir}/tdbc%{version}/libtdbcstub%{version}.a
%{_prefix}/lib/tdbcConfig.sh
%{_mandir}/man3/Tdbc_Init.3*
