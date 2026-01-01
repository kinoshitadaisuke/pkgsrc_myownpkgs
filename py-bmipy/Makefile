# $NetBSD$

DISTNAME=	bmipy-2.0.1
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	geography python
MASTER_SITES=	${MASTER_SITE_PYPI:=b/bmipy/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/bmipy/
COMMENT=	Python bindings for the CSDMS Basic Model Interface
LICENSE=	mit

USE_LANGUAGES=	# none

DEPENDS+=	${PYPKGPREFIX}-numpy>=0:../../math/py-numpy

post-install:
	cd ${DESTDIR}${PREFIX}/bin && \
	${MV} bmipy-render bmipy-render-${PYVERSSUFFIX} || ${TRUE}

.include "../../math/py-numpy/buildlink3.mk"
.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
