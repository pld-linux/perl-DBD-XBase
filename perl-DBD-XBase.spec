#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	DBD
%define	pnam	XBase
Summary:	XBase - Reading and writing the DBF files from Perl
Summary(pl):	XBase - Czytanie i zapisywanie plików DBF z poziomu Perla
Name:		perl-DBD-XBase
Version:	0.231
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-DBI
%endif
BuildRequires:	rpm-perlprov >= 4.0.2-104
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
Ten modu³ mo¿e czytaæ i zapisywaæ pliki baz danych XBase, znane jako
dbf w ¶wiecie dBase i FoxPro. Mo¿e tak¿e czytaæ w razie potrzeby pola
memo w plików dbt i fpt. Kod w fazie alpha czytaj±cy indeksy ndx, ntx,
mdx, idx i cdx jest dostêpny do testowania - wiêcej w DBD::Index(3).
Modu³ XBase udostêpnia prosty natywny interfejs do plików XBase.
Wiêcej o zgodnym z DBI dostêpie do baz danych mo¿na dowiedzieæ siê z
modu³ów i stron manuala DBD::XBase i DBI.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

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
%attr(755,root,root) %{_bindir}/dbfdump
%{perl_sitelib}/DBD/XBase.pm
%{perl_sitelib}/XBase.pm
%{perl_sitelib}/XBase
%{_mandir}/man[13]/*
%{_examplesdir}/%{name}-%{version}
