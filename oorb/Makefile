# $NetBSD$

DISTNAME=	oorb-1.3.0
CATEGORIES=	math
MASTER_SITES=	${MASTER_SITE_GITHUB:=oorb/}
GITHUB_TAG=	refs/tags/v${PKGVERSION_NOREV}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/oorb/oorb/
COMMENT=	Open-source orbit-computation package for Solar System objects
LICENSE=	gpl-3.0

WRKSRC=	${WRKDIR}/${DISTNAME}

USE_LANGUAGES+=	fortran

DEPENDS+=	bash>=0:../../shells/bash
DEPENDS+=	curl>=0:../../www/curl
DEPENDS+=	gcc12>=0:../../lang/gcc12
DEPENDS+=	ghostscript-agpl>=0:../../print/ghostscript-agpl
DEPENDS+=	gmake>=0:../../devel/gmake
DEPENDS+=	gnuplot>=0:../../graphics/gnuplot
DEPENDS+=	dvipsk>=0:../../print/dvipsk
DEPENDS+=	tex-ae>=0:../../fonts/tex-ae
DEPENDS+=	tex-acronym>=0:../../print/tex-acronym
DEPENDS+=	tex-bigfoot>=0:../../print/tex-bigfoot

do-configure:
	cd ${WRKSRC}; \
	bash ./configure gfortran opt

pre-build:
	cd ${WRKSRC}/doc; \
	latex OpenOrb_Tutorial.tex; \
	latex OpenOrb_Tutorial.tex; \
	dvips OpenOrb_Tutorial.dvi; \
	ps2pdfwr OpenOrb_Tutorial.ps; \

do-build:
	cd ${WRKSRC}/build; \
	gmake

post-build:
	cd ${WRKSRC}/data/JPL_ephemeris; \
	gmake
	
pre-install:
	mkdir -p ${DESTDIR}${PREFIX}/bin; \
	mkdir -p ${DESTDIR}${PREFIX}/etc/oorb; \
	mkdir -p ${DESTDIR}${PREFIX}/lib; \
	mkdir -p ${DESTDIR}${PREFIX}/share/oorb; \
	mkdir -p ${DESTDIR}${PREFIX}/share/oorb/gnuplot; \

do-install:
	${CP} ${WRKSRC}/bin/ephemeris_linking ${DESTDIR}${PREFIX}/bin; \
	${CP} ${WRKSRC}/bin/oorb ${DESTDIR}${PREFIX}/bin; \
	${CP} ${WRKSRC}/bin/orbit_linking ${DESTDIR}${PREFIX}/bin; \
	${CP} ${WRKSRC}/data/ET-UT.dat ${DESTDIR}${PREFIX}/share/oorb; \
	${CP} ${WRKSRC}/data/OBSCODE.dat ${DESTDIR}${PREFIX}/share/oorb; \
	${CP} ${WRKSRC}/data/TAI-UTC.dat ${DESTDIR}${PREFIX}/share/oorb; \
	${CP} ${WRKSRC}/data/de430.dat ${DESTDIR}${PREFIX}/share/oorb; \
	${CP} ${WRKSRC}/doc/OpenOrb_Tutorial.pdf ${DESTDIR}${PREFIX}/share/oorb; \
	${CP} ${WRKSRC}/lib/liboorb.a ${DESTDIR}${PREFIX}/lib; \
	${CP} ${WRKSRC}/lib/liboorb.so ${DESTDIR}${PREFIX}/lib; \
	${CP} ${WRKSRC}/main/oorb.conf ${DESTDIR}${PREFIX}/etc/oorb; \
	${CP} ${WRKSRC}/gnuplot/cos_plot_car.gp ${DESTDIR}${PREFIX}/share/oorb/gnuplot; \
	${CP} ${WRKSRC}/gnuplot/cos_plot_kep.gp ${DESTDIR}${PREFIX}/share/oorb/gnuplot; \
	${CP} ${WRKSRC}/gnuplot/ls_plot.gp ${DESTDIR}${PREFIX}/share/oorb/gnuplot; \
	${CP} ${WRKSRC}/gnuplot/sor_plot_car.gp ${DESTDIR}${PREFIX}/share/oorb/gnuplot; \
	${CP} ${WRKSRC}/gnuplot/sor_plot_kep.gp ${DESTDIR}${PREFIX}/share/oorb/gnuplot; \
	${CP} ${WRKSRC}/gnuplot/sor_plot_kep_nolog.gp ${DESTDIR}${PREFIX}/share/oorb/gnuplot; \
	${CP} ${WRKSRC}/gnuplot/sor_plot_range.gp ${DESTDIR}${PREFIX}/share/oorb/gnuplot; \
	${CP} ${WRKSRC}/gnuplot/vomcmc_plot_car.gp ${DESTDIR}${PREFIX}/share/oorb/gnuplot; \
	${CP} ${WRKSRC}/gnuplot/vomcmc_plot_kep.gp ${DESTDIR}${PREFIX}/share/oorb/gnuplot; \
	${CP} ${WRKSRC}/gnuplot/vov_plot_car.gp ${DESTDIR}${PREFIX}/share/oorb/gnuplot; \
	${CP} ${WRKSRC}/gnuplot/vov_plot_kep.gp ${DESTDIR}${PREFIX}/share/oorb/gnuplot; \

# url2pkg-marker (please do not remove this line.)
.include "../../math/lapack/buildlink3.mk"
.include "../../lang/gcc12/buildlink3.mk"
.include "../../mk/bsd.pkg.mk"
