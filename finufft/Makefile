# $NetBSD$

GITHUB_PROJECT=	finufft
DISTNAME=	2.2.0
GITHUB_TAG=	refs/tags/v${PKGVERSION_NOREV}
PKGNAME=	${GITHUB_PROJECT}-${DISTNAME}
CATEGORIES=	math
MASTER_SITES=	${MASTER_SITE_GITHUB:=flatironinstitute/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/flatironinstitute/finufft/
COMMENT=	Non-uniform fast Fourier transform library
LICENSE=	apache-2.0

USE_LANGUAGES=	c c++ fortran

WRKSRC=	${WRKDIR}/${GITHUB_PROJECT}-${DISTNAME}

DEPENDS+=	fftw>=0:../../math/fftw

.include "../../math/fftw/buildlink3.mk"
.include "../../devel/cmake/build.mk"
.include "../../mk/bsd.pkg.mk"
