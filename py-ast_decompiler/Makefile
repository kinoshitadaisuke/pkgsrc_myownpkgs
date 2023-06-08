# $NetBSD$

DISTNAME=	ast_decompiler-0.7.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=a/ast_decompiler/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/ast_decompiler/
COMMENT=	Python module to decompile AST to Python code
LICENSE=	python-software-foundation

USE_LANGUAGES=	# none

PYTHON_VERSIONS_INCOMPATIBLE=	27

DEPENDS+=	${PYPKGPREFIX}-flit_core>=3.4:../../devel/py-flit_core

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
