#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	DBD
%define	pnam	XBase
Summary:	XBase - reading and writing the DBF files from Perl
Summary(pl):	XBase - czytanie i zapisywanie plik�w DBF z poziomu Perla
Name:		perl-DBD-XBase
Version:	0.241
Release:	1
# same as Perl
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ed36f8722f09406d35c8af801fa78c3b
BuildRequires:	perl-devel >= 5.8
%if %{with tests}
BuildRequires:	perl-DBI
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module can read and write XBase database files, known as dbf in
dBase and FoxPro world. It also reads memo fields from the dbt and
fpt files, if needed. An alpha code of reading index support for ndx,
ntx, mdx, idx and cdx is available for testing - see the DBD::Index(3)
man page. Module XBase provides simple native interface to XBase
files. For DBI compliant database access, see the DBD::XBase and DBI
modules and their man pages.

%description -l pl
Ten modu� mo�e czyta� i zapisywa� pliki baz danych XBase, znane jako
dbf w �wiecie dBase i FoxPro. Mo�e tak�e czyta� w razie potrzeby pola
memo w plik�w dbt i fpt. Kod w fazie alpha czytaj�cy indeksy ndx, ntx,
mdx, idx i cdx jest dost�pny do testowania - wi�cej w DBD::Index(3).
Modu� XBase udost�pnia prosty natywny interfejs do plik�w XBase.
Wi�cej o zgodnym z DBI dost�pie do baz danych mo�na dowiedzie� si� z
modu��w i stron manuala DBD::XBase i DBI.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a eg/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README ToDo
%attr(755,root,root) %{_bindir}/*dump
%{perl_vendorlib}/DBD/XBase.pm
%{perl_vendorlib}/XBase.pm
%{perl_vendorlib}/XBase
%{_mandir}/man[13]/*
%{_examplesdir}/%{name}-%{version}
