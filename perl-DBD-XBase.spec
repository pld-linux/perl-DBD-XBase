#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	DBD
%define		pnam	XBase
Summary:	XBase - reading and writing the DBF files from Perl
Summary(pl.UTF-8):	XBase - czytanie i zapisywanie plików DBF z poziomu Perla
Name:		perl-DBD-XBase
Version:	0.241
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ed36f8722f09406d35c8af801fa78c3b
BuildRequires:	perl-devel >= 1:5.8.0
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

%description -l pl.UTF-8
Ten moduł może czytać i zapisywać pliki baz danych XBase, znane jako
dbf w świecie dBase i FoxPro. Może także czytać w razie potrzeby pola
memo w plików dbt i fpt. Kod w fazie alpha czytający indeksy ndx, ntx,
mdx, idx i cdx jest dostępny do testowania - więcej w DBD::Index(3).
Moduł XBase udostępnia prosty natywny interfejs do plików XBase.
Więcej o zgodnym z DBI dostępie do baz danych można dowiedzieć się z
modułów i stron manuala DBD::XBase i DBI.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a eg/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# get rid of pod documentation
rm -f $RPM_BUILD_ROOT%{perl_vendorlib}/XBase/*.pod

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
